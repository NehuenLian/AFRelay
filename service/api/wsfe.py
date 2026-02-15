from fastapi import APIRouter, Depends

from service.api.request_models.fe_comp_consultar import FECompConsultar
from service.api.request_models.fecae_solicitar import FECAESolicitar
from service.api.request_models.fecaea_reg_informativo import \
    FECAEARegInformativo
from service.api.request_models.simple_models import (
    FECAEAConsultar, FECAEASinMovimientoConsultar, FECAEASinMovimientoInformar,
    FECAEASolicitar, FECompTotXRequest, FECompUltimoAutorizado,
    FEParamGetActividades, FEParamGetCondicionIvaReceptor,
    FEParamGetCotizacion, FEParamGetPtosVenta, FEParamGetTiposCbte,
    FEParamGetTiposConcepto, FEParamGetTiposDoc, FEParamGetTiposIva,
    FEParamGetTiposMonedas, FEParamGetTiposOpcional, FEParamGetTiposPaises,
    FEParamGetTiposTributos)
from service.api.response_models.common import APIErrorResponseModel
from service.api.response_models.fe_comp_consultar import \
    FECompConsultarResponse
from service.api.response_models.fecae_solicitar import FECAESolicitarResponse
from service.api.response_models.simple_models import (
    FECompTotXRequestResponse, FECompUltimoAutorizadoResponse)
from service.payload_builder.builder import add_auth_to_payload
from service.soap_client.async_client import WSFEClientManager
from service.soap_client.wsdl.wsdl_manager import get_wsfe_wsdl
from service.soap_client.wsfe import consult_afip_wsfe
from service.utils.jwt_validator import verify_token
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml

router = APIRouter()
afip_wsdl = get_wsfe_wsdl()


@router.post("/wsfe/FECAESolicitar", response_model=FECAESolicitarResponse | APIErrorResponseModel)
async def fecae_solicitar(data: FECAESolicitar ,jwt = Depends(verify_token)) -> dict:
    
    logger.info("Received request to generate invoice at /wsfe/FECAESolicitar")

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAESolicitar(**data)

    result = await consult_afip_wsfe(make_request, "FECAESolicitar")
    return result


@router.post("/wsfe/FECompTotXRequest", response_model=FECompTotXRequestResponse | APIErrorResponseModel)
async def fecomp_totx_request(data: FECompTotXRequest, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompTotXRequest(**data)
    
    result = await consult_afip_wsfe(make_request, "FECompTotXRequest")
    return result


@router.post("/wsfe/FECompUltimoAutorizado", response_model=FECompUltimoAutorizadoResponse | APIErrorResponseModel)
async def fe_comp_ultimo_autorizado(data: FECompUltimoAutorizado, jwt = Depends(verify_token)) -> dict:
    logger.info("Received request to generate invoice at /wsfe/FECompUltimoAutorizado")

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompUltimoAutorizado(**data)

    result = await consult_afip_wsfe(make_request, "FECompUltimoAutorizado")
    return result


@router.post("/wsfe/FECompConsultar", response_model=FECompConsultarResponse | APIErrorResponseModel)
async def fe_comp_consultar(comp_info: FECompConsultar, jwt = Depends(verify_token)) -> dict:
    logger.info("Received request to query specific invoice at /wsfe/FECompConsultar")

    data = comp_info.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompConsultar(**data)

    result = await consult_afip_wsfe(make_request, "FECompConsultar")
    return result


@router.post("/wsfe/FECAEARegInformativo")
async def fecaea_reg_informativo(data: FECAEARegInformativo, jwt = Depends(verify_token)) -> dict:
    
    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEARegInformativo(**data)

    result = await consult_afip_wsfe(make_request, "FECAEARegInformativo")
    return result


@router.post("/wsfe/FECAEASolicitar")
async def fecaea_solicitar(data: FECAEASolicitar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASolicitar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASolicitar")
    return result


@router.post("/wsfe/FECAEASinMovimientoConsultar")
async def fecaea_sin_movimiento_consultar(data: FECAEASinMovimientoConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASinMovimientoConsultar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASinMovimientoConsultar")
    return result


@router.post("/wsfe/FECAEASinMovimientoInformar")
async def fecaea_sin_movimiento_informar(data: FECAEASinMovimientoInformar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASinMovimientoInformar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASinMovimientoInformar")
    return result


@router.post("/wsfe/FECAEAConsultar")
async def fecaea_consultar(data: FECAEAConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEAConsultar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEAConsultar")
    return result


@router.post("/wsfe/FEParamGetCotizacion")
async def fe_param_get_cotization(data: FEParamGetCotizacion, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetCotizacion(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetCotizacion")
    return result


@router.post("/wsfe/FEParamGetTiposTributos")
async def fe_param_get_tipos_tributos(data: FEParamGetTiposTributos, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposTributos(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposTributos")
    return result


@router.post("/wsfe/FEParamGetTiposMonedas")
async def fe_param_get_tipos_monedas(data: FEParamGetTiposMonedas, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposMonedas(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposMonedas")
    return result


@router.post("/wsfe/FEParamGetTiposIva")
async def fe_param_get_tipos_iva(data: FEParamGetTiposIva, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposIva(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposIva")
    return result


@router.post("/wsfe/FEParamGetTiposOpcional")
async def fe_param_get_tipos_opcional(data: FEParamGetTiposOpcional, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposOpcional(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposOpcional")
    return result


@router.post("/wsfe/FEParamGetTiposConcepto")
async def fe_param_get_tipos_concepto(data: FEParamGetTiposConcepto, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposConcepto(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposConcepto")
    return result


@router.post("/wsfe/FEParamGetPtosVenta")
async def fe_param_get_ptos_venta(data: FEParamGetPtosVenta, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetPtosVenta(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetPtosVenta")
    return result


@router.post("/wsfe/FEParamGetTiposCbte")
async def fe_param_get_tipos_cbte(data: FEParamGetTiposCbte, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposCbte(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposCbte")
    return result


@router.post("/wsfe/FEParamGetCondicionIvaReceptor")
async def fe_param_get_condicion_iva_receptor(data: FEParamGetCondicionIvaReceptor, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetCondicionIvaReceptor(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetCondicionIvaReceptor")
    return result


@router.post("/wsfe/FEParamGetTiposDoc")
async def fe_param_get_tipos_doc(data: FEParamGetTiposDoc, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposDoc(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposDoc")
    return result


@router.post("/wsfe/FEParamGetTiposPaises")
async def fe_param_get_tipos_paises(data: FEParamGetTiposPaises, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposPaises(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposPaises")
    return result


@router.post("/wsfe/FEParamGetActividades")
async def fe_param_get_actividades(data: FEParamGetActividades, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetActividades(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetActividades")
    return result