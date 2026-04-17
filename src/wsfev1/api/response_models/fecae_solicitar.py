from typing import Dict

from pydantic import BaseModel, ConfigDict, Field


class Observaciones(BaseModel):
    Code: int
    Msg: str 

class Obs(BaseModel):
    Observaciones: list[Observaciones] | Dict

class Evt(BaseModel):
    Code: int
    Msg: str

class Events(BaseModel):
    Evt: list[Evt] | Dict

class Err(BaseModel):
    Code: int
    Msg: str

class Errors(BaseModel):
    Err: list[Err] | Dict

class FECAEDetResponse(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    Concepto: int
    DocTipo: int
    DocNro: int
    CbteDesde: int
    CbteHasta: int
    CbteFch: str
    Resultado: str
    CAE: str | None = None
    CAEFchVto: str | None = None

    obs : Obs | None = Field(None, alias="Obs")

class FeDetResp(BaseModel):
    FECAEDetResponse : list[FECAEDetResponse] | Dict

class FeCabResp(BaseModel):
    Cuit: int
    PtoVta: int
    CbteTipo: int
    FchProceso: str
    CantReg: int
    Resultado: str
    Reproceso: str | None = None

class FECAESolicitarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    FeCabResp: FeCabResp
    FeDetResp: FeDetResp

    errors: Errors | None = Field(None, alias="Errors")
    events: Events | None = Field(None, alias="Events")

class FECAESolicitarResponse(BaseModel):
    FECAESolicitarResult: FECAESolicitarResult

class FECAESolicitarMainClass(BaseModel):
    FECAESolicitarResponse: FECAESolicitarResponse

class FECAESolicitarFullResponse(BaseModel):
    status: str
    response: FECAESolicitarMainClass 