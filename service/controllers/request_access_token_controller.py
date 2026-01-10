from service.crypto.sign import get_binary_cms, sign_login_ticket_request
from service.soap_client.wsaa import login_cms
from service.time.time_management import generate_ntp_timestamp
from service.utils.logger import logger
from service.xml_management.xml_builder import (
    build_login_ticket_request, parse_and_save_loginticketresponse, save_xml)


async def generate_afip_access_token() -> None:

    logger.info("Generating a new access token...")

    root = build_login_ticket_request(generate_ntp_timestamp)
    save_xml(root, "loginTicketRequest.xml")
    sign_login_ticket_request()
    b64_cms = get_binary_cms()
    login_ticket_response = await login_cms(b64_cms)

    if login_ticket_response["status"] == "success":
        parse_and_save_loginticketresponse(login_ticket_response["response"], save_xml)
        logger.info("Token generated successfully.")
        return

    logger.error("Failed to generate access token.")