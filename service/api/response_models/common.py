
from pydantic import BaseModel


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
