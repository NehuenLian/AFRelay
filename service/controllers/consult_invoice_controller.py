from service.payload_builder.builder import build_auth
from service.soap_client.async_client import WSFEClientManager
from service.soap_client.wsdl.wsdl_manager import get_wsfe_wsdl
from service.soap_client.wsfe import consult_afip_wsfe
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml

afip_wsdl = get_wsfe_wsdl()

async def consult_specific_invoice(comp_info: dict) -> dict:

    logger.info(f"Consulting info about an specific invoice: CbteNro={comp_info['CbteNro']}")

    token, sign = extract_token_and_sign_from_xml()

    cuit = comp_info["Cuit"]
    auth = build_auth(token, sign, cuit)

    fecomp_req = {
        'PtoVta': comp_info["PtoVta"],
        'CbteTipo': comp_info["CbteTipo"],
        'CbteNro': comp_info["CbteNro"],
    }

    async def fe_comp_consultar():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompConsultar(auth, fecomp_req)

    invoice_result = await consult_afip_wsfe(fe_comp_consultar, "FECompConsultar")
    return invoice_result