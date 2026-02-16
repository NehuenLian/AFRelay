from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import (Errors, Events,
                                                FECAEAGetResponse,
                                                FECAEASinMov)

# ========================================================

class FECompTotXRequestResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    RegXReq: int

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompTotXRequestResponse(BaseModel):
    status: str
    response: FECompTotXRequestResult

# ========================================================

class FECompUltimoAutorizadoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    PtoVta: int
    CbteTipo: int
    CbteNro: int | None = None

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompUltimoAutorizadoResponse(BaseModel):
    status: str
    response: FECompUltimoAutorizadoResult

# ========================================================

class FECAEASinMovimientoConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_sin_mov: list[FECAEASinMov] | None = Field(None, alias="FECAEASinMov")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASinMovimientoConsultarResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoConsultarResult

# ========================================================

class FECAEASinMovimientoInformarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_sin_mov: list[FECAEASinMov] | None = Field(None, alias="FECAEASinMov")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASinMovimientoInformarResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoConsultarResult

# ========================================================

class FECAEAConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_get_response: FECAEAGetResponse | None = Field(None, alias="FECAEAGetResponse")

class FECAEAConsultarResponse(BaseModel):
    status: str 
    response: FECAEAConsultarResult

# ========================================================

class ResultGet(BaseModel):
    MonId: str
    MonCotiz: float
    FchCotiz: str

class FECotizacionResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    errors: Errors | None = Field(None, alias="Errors")
    events: Events | None = Field(None, alias="Events")

class FEParamGetCotizacionResponse(BaseModel):
    status: str   
    response: FECotizacionResult

# ========================================================

class TributoTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposTributosResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    tributo_tipo: list[TributoTipo] | None = Field(None, alias="TributoTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposTributosResponse(BaseModel):
    status: str
    response: FEParamGetTiposTributosResult

# ========================================================

class Moneda(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposMonedasResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    moneda: list[Moneda] | None = Field(None, alias="Moneda")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposMonedasResponse(BaseModel):
    status: str
    response: FEParamGetTiposMonedasResult

# ========================================================

class IvaTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposIvaResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    iva_tipo: list[IvaTipo] | None = Field(None, alias="IvaTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposIvaResponse(BaseModel):
    status: str
    response: FEParamGetTiposIvaResult

# ========================================================

class OpcionalTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposOpcionalResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    opcional_tipo: list[OpcionalTipo] | None = Field(None, alias="OpcionalTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposOpcionalResponse(BaseModel):
    status: str
    response: FEParamGetTiposOpcionalResult

# ========================================================

class ConceptoTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposConceptoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    concepto_tipo: list[ConceptoTipo] | None = Field(None, alias="ConceptoTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposConceptoResponse(BaseModel):
    status: str
    response: FEParamGetTiposConceptoResult

# ========================================================

class PtoVenta(BaseModel):
    Id: int
    EmisionTipo: str | None = None
    Bloqueado: str | None = None
    FchBaja: str | None = None

class FEParamGetPtosVentaResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    pto_venta: list[PtoVenta] | None = Field(None, alias="PtoVenta")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetPtosVentaResponse(BaseModel):
    status: str
    response: FEParamGetPtosVentaResult

# ========================================================

class CbteTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposCbteResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    cbte_tipo: list[CbteTipo] | None = Field(None, alias="CbteTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposCbteResponse(BaseModel):
    status: str
    response: FEParamGetTiposCbteResult

# ========================================================

class CondicionIvaReceptor(BaseModel):
    Id: int
    Desc: str | None = None
    Cpm_Clase: str | None = None

class FEParamGetCondicionIvaReceptorResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    condicion_iva_receptor: list[CondicionIvaReceptor] | None = Field(None, alias="CondicionIvaReceptor")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetCondicionIvaReceptorResponse(BaseModel):
    status: str
    response: FEParamGetCondicionIvaReceptorResult

# ========================================================

class DocTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposDocResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    doc_tipo: list[DocTipo] | None = Field(None, alias="DocTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposDocResponse(BaseModel):
    status: str
    response: FEParamGetTiposDocResult

# ========================================================

class PaisTipo(BaseModel):
    Id: int
    Desc: str | None = None

class FEParamGetTiposPaisesResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    pais_tipo: list[PaisTipo] | None = Field(None, alias="PaisTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposPaisesResponse(BaseModel):
    status: str
    response: FEParamGetTiposPaisesResult

# ========================================================

class ActividadesTipo(BaseModel):
    Id: int
    Orden: int
    Desc: str | None = None

class FEParamGetActividadesResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    actividades_tipo: list[ActividadesTipo] | None = Field(None, alias="ActividadesTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetActividadesResponse(BaseModel):
    status: str
    response: FEParamGetActividadesResult

# ========================================================