
from pydantic import BaseModel, Field


class Obs(BaseModel):
    Code: int
    Msg: str | None = None

class Observaciones(BaseModel):
    obs: list[Obs] | None = Field(None, alias="Obs")

class Evt(BaseModel):
    Code: int
    Msg: str

class Events(BaseModel):
    Evt: list[Evt]

class Err(BaseModel):
    Code: int
    Msg: str

class Errors(BaseModel):
    Err: list[Err]


######### Infrastructure #########
class ErrorDetails(BaseModel):
    method: str
    error_type: str
    details: str

class APIErrorResponseModel(BaseModel):
    status: str
    error: ErrorDetails
