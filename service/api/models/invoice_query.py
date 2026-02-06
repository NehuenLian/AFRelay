from pydantic import BaseModel


class InvoiceBaseQuery(BaseModel):
    Cuit: int

class FECAEAConsultar(InvoiceBaseQuery):
    Periodo: int
    Orden: int

class FECompConsultar(InvoiceBaseQuery):
    PtoVta: int
    CbteTipo: int
    CbteNro: int

class FECompUltimoAutorizado(InvoiceBaseQuery):
    PtoVta: int
    CbteTipo: int
