import html
import os
from datetime import datetime, timezone

from jinja2 import Template
from lxml import etree

from src.shared.paths_config import paths
from src.shared.utils.logger import logger
from src.wsaa.soap_client import templates


def build_login_ticket_request(time_provider) -> "etree._Element":

    root = etree.Element("loginTicketRequest")
    header = etree.SubElement(root, "header")
    unique_id = etree.SubElement(header, "uniqueId")
    generation_time_label = etree.SubElement(header, "generationTime")
    expiration_time_label = etree.SubElement(header, "expirationTime")
    service = etree.SubElement(root, "service")

    actual_hour, generation_time, expiration_time = time_provider()

    unique_id.text = str(actual_hour)
    generation_time_label.text = str(generation_time)
    expiration_time_label.text = str(expiration_time)
    service.text = "wsfe"

    return root

def parse_and_save_loginticketresponse(login_ticket_response: str, xml_saver) -> None:

    root = etree.fromstring(login_ticket_response.encode("utf-8"))
    xml_no_cleaned = root.find('.//{http://wsaa.view.sua.dvadac.desein.afip.gov}loginCmsReturn').text
    xml_real = etree.fromstring(html.unescape(xml_no_cleaned).encode("utf-8"))

    xml_saver(xml_real, "loginTicketResponse.xml")

def is_expired(xml_name: str, time_provider) -> bool:

    logger.debug(f"Running is_expired() function for {xml_name}")

    _, actual_hour, _ = time_provider()

    actual_dt = datetime.strptime(str(actual_hour), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

    path = paths.get_afip_paths().base_xml / xml_name
    tree = etree.parse(path)
    root = tree.getroot()
    expiration_time_label = root.find(".//expirationTime")
    expiration_time_str = expiration_time_label.text

    expiration_dt_raw = datetime.fromisoformat(expiration_time_str)
    expiration_dt = expiration_dt_raw.astimezone(timezone.utc)

    if actual_dt >= expiration_dt:
        return True
    else:
        return False

def save_xml(root, xml_name: str) -> None:
    
    path = paths.get_afip_paths().base_xml / xml_name
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tree = etree.ElementTree(root)
    tree.write(path, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    logger.info(f"{xml_name} successfully saved.")

def xml_exists(xml_name: str) -> bool:
    xml_path = paths.get_afip_paths().base_xml / xml_name

    if os.path.exists(xml_path):
        return True
    else:
        return False

def build_xml_to_send(b64_cms: str) -> str:

    loginCms_xml = templates.loginCms
    loginCms_xml_stripped = loginCms_xml.strip()
    template = Template(loginCms_xml_stripped)

    return template.render(CMS=b64_cms)