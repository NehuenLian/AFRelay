from service.payload_builder.builder import add_auth_to_payload
from service.soap_client.async_client import WSFEClientManager
from service.soap_client.wsdl.wsdl_manager import get_wsfe_wsdl
from service.soap_client.wsfe import consult_afip_wsfe
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml

afip_wsdl = get_wsfe_wsdl()

async def request_invoice_controller(sale_data: dict) -> dict:

    logger.info("Generating invoice...")
    token, sign = extract_token_and_sign_from_xml()
    invoice_with_auth = add_auth_to_payload(sale_data, token, sign)

    async def fecae_solicitar():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAESolicitar(invoice_with_auth['Auth'], invoice_with_auth['FeCAEReq'])

    invoice_result = await consult_afip_wsfe(fecae_solicitar, "FECAESolicitar")
    return invoice_result
