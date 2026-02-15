from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import Errors, Events


class FECompTotXRequestResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    RegXReq: int

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompTotXRequestResponse(BaseModel):
    status: str
    response: FECompTotXRequestResult


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