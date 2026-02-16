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