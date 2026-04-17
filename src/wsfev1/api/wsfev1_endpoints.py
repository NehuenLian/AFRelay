from fastapi import APIRouter, Depends

from src.shared.api.jwt_validator import verify_token
from src.shared.api.response_models.errors import APIErrorResponseModel
from src.shared.payload_builder.builder import add_auth_to_payload
from src.shared.utils.logger import logger
from src.wsfev1.api.request_models.fe_comp_consultar import FECompConsultar
from src.wsfev1.api.request_models.fecae_solicitar import FECAESolicitar
from src.wsfev1.api.request_models.fecaea_reg_informativo import \
    FECAEARegInformativo
from src.wsfev1.api.request_models.simple_models import (
    FECAEAConsultar, FECAEASinMovimientoConsultar, FECAEASinMovimientoInformar,
    FECAEASolicitar, FECompTotXRequest, FECompUltimoAutorizado,
    FEParamGetActividades, FEParamGetCondicionIvaReceptor,
    FEParamGetCotizacion, FEParamGetPtosVenta, FEParamGetTiposCbte,
    FEParamGetTiposConcepto, FEParamGetTiposDoc, FEParamGetTiposIva,
    FEParamGetTiposMonedas, FEParamGetTiposOpcional, FEParamGetTiposPaises,
    FEParamGetTiposTributos)
from src.wsfev1.api.response_models import simple_models
from src.wsfev1.api.response_models.fe_comp_consultar import \
    FECompConsultarFullResponse
from src.wsfev1.api.response_models.fecae_solicitar import \
    FECAESolicitarFullResponse
from src.wsfev1.api.response_models.fecaea_reg_informativo import \
    FECAEARegInformativoResponse
from src.wsfev1.controllers.readiness_health_controller import \
    readiness_health_check
from src.wsfev1.soap_client import templates
from src.wsfev1.soap_client.url_manager import get_wsfe_url
from src.wsfev1.soap_client.wsfev1 import consult_afip_wsfev1
from src.wsfev1.xml_management.xml_builder import (
    build_xml, extract_token_and_sign_from_xml)

router = APIRouter()
afip_wsdl = get_wsfe_url()


@router.get("/wsfev1/health/readiness")
async def readiness() -> dict:

    logger.info(f"Consulting WSFE dummy method (health check).")
    status = await readiness_health_check()
    return status


@router.post("/wsfev1/FECAESolicitar", response_model=FECAESolicitarFullResponse | APIErrorResponseModel)
async def fecae_solicitar(data: FECAESolicitar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAESolicitar)

    response = await consult_afip_wsfev1(xml_string, "FECAESolicitar")
    return response


@router.post("/wsfev1/FECompTotXRequest", response_model = simple_models.FECompTotXRequestFullResponse | APIErrorResponseModel)
async def fe_comp_totx_request(data: FECompTotXRequest, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECompTotXRequest)

    response = await consult_afip_wsfev1(xml_string, "FECompTotXRequest")
    return response


@router.post("/wsfev1/FECompUltimoAutorizado", response_model=simple_models.FECompUltimoAutorizadoFullResponse | APIErrorResponseModel)
async def fe_comp_ultimo_autorizado(data: FECompUltimoAutorizado, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECompUltimoAutorizado)

    response = await consult_afip_wsfev1(xml_string, "FECompUltimoAutorizado")
    return response

@router.post("/wsfev1/FECompConsultar", response_model=FECompConsultarFullResponse | APIErrorResponseModel)
async def fe_comp_consultar(comp_info: FECompConsultar, jwt = Depends(verify_token)) -> dict:

    logger.info("Received request to query invoice at /wsfe/FECompConsultar")

    data = comp_info.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECompConsultar)

    response = await consult_afip_wsfev1(xml_string, "FECompConsultar")
    return response


@router.post("/wsfev1/FECAEARegInformativo", response_model=FECAEARegInformativoResponse | APIErrorResponseModel)
async def fecaea_reg_informativo(data: FECAEARegInformativo, jwt = Depends(verify_token)) -> dict:
    
    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAEARegInformativo)

    response = await consult_afip_wsfev1(xml_string, "FECAEARegInformativo")
    return response

@router.post("/wsfev1/FECAEASolicitar", response_model = simple_models.FECAEASolicitarFullResponse | APIErrorResponseModel)
async def fecaea_solicitar(data: FECAEASolicitar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAEASolicitar)

    response = await consult_afip_wsfev1(xml_string, "FECAEASolicitar")
    return response


@router.post("/wsfev1/FECAEASinMovimientoConsultar", response_model = simple_models.FECAEASinMovimientoConsultarFullResponse | APIErrorResponseModel)
async def fecaea_sin_movimiento_consultar(data: FECAEASinMovimientoConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAEASinMovimientoConsultar)

    response = await consult_afip_wsfev1(xml_string, "FECAEASinMovimientoConsultar")
    return response


@router.post("/wsfev1/FECAEASinMovimientoInformar", response_model = simple_models.FECAEASinMovimientoInformarFullResponse | APIErrorResponseModel)
async def fecaea_sin_movimiento_informar(data: FECAEASinMovimientoInformar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAEASinMovimientoInformar)

    response = await consult_afip_wsfev1(xml_string, "FECAEASinMovimientoInformar")
    return response


@router.post("/wsfev1/FECAEAConsultar", response_model = simple_models.FECAEAConsultarFullResponse | APIErrorResponseModel)
async def fecaea_consultar(data: FECAEAConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FECAEAConsultar)

    response = await consult_afip_wsfev1(xml_string, "FECAEAConsultar")
    return response


@router.post("/wsfev1/FEParamGetCotizacion", response_model = simple_models.FEParamGetCotizacionFullResponse | APIErrorResponseModel)
async def fe_param_get_cotization(data: FEParamGetCotizacion, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetCotizacion)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetCotizacion")
    return response


@router.post("/wsfev1/FEParamGetTiposTributos", response_model = simple_models.FEParamGetTiposTributosFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_tributos(data: FEParamGetTiposTributos, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposTributos)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposTributos")
    return response


@router.post("/wsfev1/FEParamGetTiposMonedas", response_model = simple_models.FEParamGetTiposMonedasFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_monedas(data: FEParamGetTiposMonedas, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposMonedas)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposMonedas")
    return response


@router.post("/wsfev1/FEParamGetTiposIva", response_model = simple_models.FEParamGetTiposIvaFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_iva(data: FEParamGetTiposIva, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposIva)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposIva")
    return response


@router.post("/wsfev1/FEParamGetTiposOpcional", response_model = simple_models.FEParamGetTiposOpcionalFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_opcional(data: FEParamGetTiposOpcional, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposOpcional)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposOpcional")
    return response


@router.post("/wsfev1/FEParamGetTiposConcepto", response_model = simple_models.FEParamGetTiposConceptoFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_concepto(data: FEParamGetTiposConcepto, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposConcepto)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposConcepto")
    return response


@router.post("/wsfev1/FEParamGetPtosVenta", response_model = simple_models.FEParamGetPtosVentaFullResponse | APIErrorResponseModel)
async def fe_param_get_ptos_venta(data: FEParamGetPtosVenta, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetPtosVenta)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetPtosVenta")
    return response


@router.post("/wsfev1/FEParamGetTiposCbte", response_model = simple_models.FEParamGetTiposCbteFullResponse| APIErrorResponseModel)
async def fe_param_get_tipos_cbte(data: FEParamGetTiposCbte, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposCbte)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposCbte")
    return response


@router.post("/wsfev1/FEParamGetCondicionIvaReceptor", response_model = simple_models.FEParamGetCondicionIvaReceptorFullResponse | APIErrorResponseModel)
async def fe_param_get_condicion_iva_receptor(data: FEParamGetCondicionIvaReceptor, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetCondicionIvaReceptor)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetCondicionIvaReceptor")
    return response

@router.post("/wsfev1/FEParamGetTiposDoc", response_model = simple_models.FEParamGetTiposDocFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_doc(data: FEParamGetTiposDoc, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposDoc)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposDoc")
    return response


@router.post("/wsfev1/FEParamGetTiposPaises", response_model = simple_models.FEParamGetTiposPaisesFullResponse | APIErrorResponseModel)
async def fe_param_get_tipos_paises(data: FEParamGetTiposPaises, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetTiposPaises)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetTiposPaises")
    return response


@router.post("/wsfev1/FEParamGetActividades", response_model = simple_models.FEParamGetActividadesFullResponse | APIErrorResponseModel)
async def fe_param_get_actividades(data: FEParamGetActividades, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    payload = add_auth_to_payload(data, token, sign)
    xml_string = build_xml(payload, templates.FEParamGetActividades)

    response = await consult_afip_wsfev1(xml_string, "FEParamGetActividades")
    return response