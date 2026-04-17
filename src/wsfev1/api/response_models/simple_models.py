from typing import Dict

from pydantic import BaseModel, ConfigDict, Field

from src.wsfev1.api.response_models.common import Errors, Events, Observaciones

# ========================================================

class FECompTotXRequestResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    RegXReq: int

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompTotXRequestResponse(BaseModel):
    FECompTotXRequestResult: FECompTotXRequestResult

class FECompTotXRequestMainClass(BaseModel):
    FECompTotXRequestResponse: FECompTotXRequestResponse

class FECompTotXRequestFullResponse(BaseModel):
    status: str
    response: FECompTotXRequestMainClass

# ========================================================

class FECompUltimoAutorizadoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    PtoVta: int
    CbteTipo: int
    CbteNro: int | None = None

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompUltimoAutorizadoResponse(BaseModel):
    FECompUltimoAutorizadoResult: FECompUltimoAutorizadoResult

class FECompUltimoAutorizadoMainClass(BaseModel):
    FECompUltimoAutorizadoResponse: FECompUltimoAutorizadoResponse

class FECompUltimoAutorizadoFullResponse(BaseModel):
    status: str
    response: FECompUltimoAutorizadoMainClass

# ========================================================

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    CAEA: str | None = None
    Periodo: int
    Orden: int
    FchVto: str | None = None
    FchVigDesde: str | None = None
    FchVigHasta: str | None = None
    FchLimiteInf: str | None = None
    FchProceso: str | None = None

    observaciones: Observaciones | None = Field(None, alias="Observaciones")

class FECAEASolicitarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(..., alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASolicitarResponse(BaseModel):
    FECAEASolicitarResult: FECAEASolicitarResult

class FECAEASolicitarMainClass(BaseModel):
    FECAEASolicitarResponse: FECAEASolicitarResponse

class FECAEASolicitarFullResponse(BaseModel):
    status: str 
    response: FECAEASolicitarMainClass

# ========================================================

class FECAEASinMov(BaseModel):
    CAEA: str
    FchProceso: str
    PtoVta: int

class ResultGet(BaseModel):
    fecaea_sin_mov: list[FECAEASinMov] | Dict | None = Field(None, alias="FECAEASinMov")

class FECAEASinMovimientoConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    errors: Errors | None = Field(None, alias="Errors")
    events: Events | None = Field(None, alias="Events")

class FECAEASinMovimientoConsultarResponse(BaseModel):
    FECAEASinMovimientoConsultarResult: FECAEASinMovimientoConsultarResult

class FECAEASinMovimientoConsultarMainClass(BaseModel):
    FECAEASinMovimientoConsultarResponse: FECAEASinMovimientoConsultarResponse

class FECAEASinMovimientoConsultarFullResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoConsultarMainClass

# ========================================================

class FECAEASinMovimientoInformarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    CAEA: str
    FchProceso: str
    PtoVta: int
    Resultado: str

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASinMovimientoInformarResponse(BaseModel):
    FECAEASinMovimientoInformarResult: FECAEASinMovimientoInformarResult

class FECAEASinMovimientoInformarMainClass(BaseModel):
    FECAEASinMovimientoInformarResponse: FECAEASinMovimientoInformarResponse

class FECAEASinMovimientoInformarFullResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoInformarMainClass

# ========================================================

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    CAEA: str | None = None
    Periodo: int
    Orden: int
    FchVto: str | None = None
    FchVigDesde: str | None = None
    FchVigHasta: str | None = None
    FchLimiteInf: str | None = None
    FchProceso: str | None = None

    observaciones: Observaciones | None = Field(None, alias="Observaciones")

class FECAEAConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_get_response: ResultGet | None = Field(None, alias="ResultGet")

class FECAEAConsultarResponse(BaseModel):
    FECAEAConsultarResult: FECAEAConsultarResult

class FECAEAConsultarMainClass(BaseModel):
    FECAEAConsultarResponse: FECAEAConsultarResponse

class FECAEAConsultarFullResponse(BaseModel):
    status: str
    response: FECAEAConsultarMainClass

# ========================================================

class ResultGet(BaseModel):
    MonId: str | None = None
    MonCotiz: float
    FchCotiz: str | None = None

class FEParamGetCotizacionResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    errors: Errors | None = Field(None, alias="Errors")
    events: Events | None = Field(None, alias="Events")

class FEParamGetCotizacionResponse(BaseModel):
    FEParamGetCotizacionResult: FEParamGetCotizacionResult

class FEParamGetCotizacionMainClass(BaseModel):
    FEParamGetCotizacionResponse: FEParamGetCotizacionResponse

class FEParamGetCotizacionFullResponse(BaseModel):
    status: str
    response: FEParamGetCotizacionMainClass

# ========================================================

class TributoTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    tributo_tipo: list[TributoTipo] | None = Field(None, alias="TributoTipo")

class FEParamGetTiposTributosResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposTributosResponse(BaseModel):
    FEParamGetTiposTributosResult: FEParamGetTiposTributosResult

class FEParamGetTiposTributosMainClass(BaseModel):
    FEParamGetTiposTributosResponse: FEParamGetTiposTributosResponse

class FEParamGetTiposTributosFullResponse(BaseModel):
    status: str 
    response: FEParamGetTiposTributosMainClass

# ========================================================

class Moneda(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    moneda: list[Moneda] | None = Field(None, alias="Moneda")

class FEParamGetTiposMonedasResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposMonedasResponse(BaseModel):
    FEParamGetTiposMonedasResult: FEParamGetTiposMonedasResult

class FEParamGetTiposMonedasMainClass(BaseModel):
    FEParamGetTiposMonedasResponse: FEParamGetTiposMonedasResponse

class FEParamGetTiposMonedasFullResponse(BaseModel):
    status: str 
    response: FEParamGetTiposMonedasMainClass

# ========================================================

class IvaTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    iva_tipo: list[IvaTipo] | None = Field(None, alias="IvaTipo")

class FEParamGetTiposIvaResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposIvaResponse(BaseModel):
    FEParamGetTiposIvaResult: FEParamGetTiposIvaResult

class FEParamGetTiposIvaMainClass(BaseModel):
    FEParamGetTiposIvaResponse: FEParamGetTiposIvaResponse

class FEParamGetTiposIvaFullResponse(BaseModel):
    status: str 
    response: FEParamGetTiposIvaMainClass

# ========================================================

class OpcionalTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    opcional_tipo: list[OpcionalTipo] | None = Field(None, alias="OpcionalTipo")

class FEParamGetTiposOpcionalResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposOpcionalResponse(BaseModel):
    FEParamGetTiposOpcionalResult: FEParamGetTiposOpcionalResult

class FEParamGetTiposOpcionalMainClass(BaseModel):
    FEParamGetTiposOpcionalResponse: FEParamGetTiposOpcionalResponse

class FEParamGetTiposOpcionalFullResponse(BaseModel):
    status: str
    response: FEParamGetTiposOpcionalMainClass

# ========================================================

class ConceptoTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    concepto_tipo: list[ConceptoTipo] | None = Field(None, alias="ConceptoTipo")

class FEParamGetTiposConceptoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposConceptoResponse(BaseModel):
    FEParamGetTiposConceptoResult: FEParamGetTiposConceptoResult

class FEParamGetTiposConceptoMainClass(BaseModel):
    FEParamGetTiposConceptoResponse: FEParamGetTiposConceptoResponse

class FEParamGetTiposConceptoFullResponse(BaseModel):
    status: str
    response: FEParamGetTiposConceptoMainClass

# ========================================================

class PtoVenta(BaseModel):
    Nro: int
    EmisionTipo: str | None = None
    Bloqueado: str | None = None
    FchBaja: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    pto_venta: list[PtoVenta] | None = Field(None, alias="PtoVenta")

class FEParamGetPtosVentaResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetPtosVentaResponse(BaseModel):
    FEParamGetPtosVentaResult: FEParamGetPtosVentaResult

class FEParamGetPtosVentaMainClass(BaseModel):
    FEParamGetPtosVentaResponse: FEParamGetPtosVentaResponse

class FEParamGetPtosVentaFullResponse(BaseModel):
    status: str
    response: FEParamGetPtosVentaMainClass

# ========================================================

class CbteTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    cbte_tipo: list[CbteTipo] | None = Field(None, alias="CbteTipo")

class FEParamGetTiposCbteResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposCbteResponse(BaseModel):
    FEParamGetTiposCbteResult: FEParamGetTiposCbteResult

class FEParamGetTiposCbteMainClass(BaseModel):
    FEParamGetTiposCbteResponse: FEParamGetTiposCbteResponse

class FEParamGetTiposCbteFullResponse(BaseModel):
    status: str
    response: FEParamGetTiposCbteMainClass

# ========================================================

class CondicionIvaReceptor(BaseModel):
    Id: int
    Desc: str | None = None
    ClaseCmp: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    condicion_iva_receptor: list[CondicionIvaReceptor] | None = Field(None, alias="CondicionIvaReceptor")

class FEParamGetCondicionIvaReceptorResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetCondicionIvaReceptorResponse(BaseModel):
    FEParamGetCondicionIvaReceptorResult: FEParamGetCondicionIvaReceptorResult

class FEParamGetCondicionIvaReceptorMainClass(BaseModel):
    FEParamGetCondicionIvaReceptorResponse: FEParamGetCondicionIvaReceptorResponse

class FEParamGetCondicionIvaReceptorFullResponse(BaseModel):
    status: str
    response: FEParamGetCondicionIvaReceptorMainClass

# ========================================================

class DocTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    doc_tipo: list[DocTipo] | None = Field(None, alias="DocTipo")

class FEParamGetTiposDocResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposDocResponse(BaseModel):
    FEParamGetTiposDocResult: FEParamGetTiposDocResult

class FEParamGetTiposDocMainClass(BaseModel):
    FEParamGetTiposDocResponse: FEParamGetTiposDocResponse

class FEParamGetTiposDocFullResponse(BaseModel):
    status: str 
    response: FEParamGetTiposDocMainClass

# ========================================================

class PaisTipo(BaseModel):
    Id: int
    Desc: str | None = None

class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    pais_tipo: list[PaisTipo] | Dict | None = Field(None, alias="PaisTipo")

class FEParamGetTiposPaisesResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposPaisesResponse(BaseModel):
    FEParamGetTiposPaisesResult: FEParamGetTiposPaisesResult

class FEParamGetTiposPaisesMainClass(BaseModel):
    FEParamGetTiposPaisesResponse: FEParamGetTiposPaisesResponse

class FEParamGetTiposPaisesFullResponse(BaseModel):
    status: str
    response: FEParamGetTiposPaisesMainClass

# ========================================================

class ActividadesTipo(BaseModel):
    Id: int
    Orden: int
    Desc: str | None = None

class ResultGet(BaseModel):
    actividades_tipo: list[ActividadesTipo] | None = Field(None, alias="ActividadesTipo")

class FEParamGetActividadesResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetActividadesResponse(BaseModel):
    FEParamGetActividadesResult: FEParamGetActividadesResult

class FEParamGetActividadesMainClass(BaseModel):
    FEParamGetActividadesResponse: FEParamGetActividadesResponse

class FEParamGetActividadesFullResponse(BaseModel):
    status: str
    response: FEParamGetActividadesMainClass

# ========================================================