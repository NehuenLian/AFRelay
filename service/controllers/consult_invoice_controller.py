from service.payload_builder.builder import build_auth
from service.soap_client.wsfe import fe_comp_consultar
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml


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

    invoice_result = await fe_comp_consultar(auth, fecomp_req)

    return invoice_result