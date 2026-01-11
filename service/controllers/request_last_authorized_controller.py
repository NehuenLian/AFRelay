from service.payload_builder.builder import build_auth
from service.soap_client.async_client import WSFEClientManager
from service.soap_client.wsdl.wsdl_manager import get_wsfe_wsdl
from service.soap_client.wsfe import consult_afip_wsfe
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml

afip_wsdl = get_wsfe_wsdl()

async def get_last_authorized_info(comp_info: dict) -> dict:

    logger.info("Consulting last authorized invoice...")

    token, sign = extract_token_and_sign_from_xml()

    cuit = comp_info["Cuit"]
    ptovta = comp_info["PtoVta"]
    cbtetipo = comp_info["CbteTipo"]

    auth = build_auth(token, sign, cuit)

    async def fe_comp_ultimo_autorizado():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompUltimoAutorizado(auth, ptovta, cbtetipo)

    last_authorized_invoice = await consult_afip_wsfe(fe_comp_ultimo_autorizado, "FECompUltimoAutorizado")
    return last_authorized_invoice