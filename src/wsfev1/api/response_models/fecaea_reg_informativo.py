from pydantic import BaseModel, ConfigDict, Field

from src.wsfev1.api.response_models.common import Errors, Events, Observaciones


class Observaciones(BaseModel):
    Code: int
    Msg: str | None = None

class FECAEADetResponse(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    Concepto: int
    DocTipo: int
    DocNro: int
    CbteDesde: int
    CbteHasta: int
    CbteFch: str | None = None
    Resultado: str | None = None
    obs: list[Observaciones] | None = Field(None, alias="Obs")

    CAEA: str | None = None

class FeDetResp(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecae_det_response: list[FECAEADetResponse] | None = Field(None, alias="FECAEADetResponse")

class FeCabResp(BaseModel):    
    Cuit: int
    PtoVta: int
    CbteTipo: int
    FchProceso: str | None = None
    CantReg: int
    Resultado: str | None = None
    Reproceso: str | None = None

class FECAEARegInformativoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fe_cab_resp: FeCabResp | None = Field(None, alias="FeCabResp")
    fe_det_resp: FeDetResp | None = Field(None, alias="FeDetResp")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEARegInformativoResponse(BaseModel):
    FECAEARegInformativoResult: FECAEARegInformativoResult

class FECAEARegInformativoMainClass(BaseModel):
    FECAEARegInformativoResponse: FECAEARegInformativoResponse

class FECAEARegInformativoFullResponse(BaseModel):
    status: str 
    response: FECAEARegInformativoMainClass | None