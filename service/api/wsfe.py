from fastapi import APIRouter, Depends

from service.api.models.fecae_solicitar import RootModel
from service.api.models.invoice_query import InvoiceBase, InvoiceQueryRequest
from service.controllers.consult_invoice_controller import \
    consult_specific_invoice
from service.controllers.request_invoice_controller import \
    request_invoice_controller
from service.controllers.request_last_authorized_controller import \
    get_last_authorized_info
from service.utils.jwt_validator import verify_token
from service.utils.logger import logger

router = APIRouter()

@router.post("/wsfe/FECAESolicitar")
async def generate_invoice(sale_data: RootModel, jwt = Depends(verify_token)) -> dict:
    
    logger.info("Received request to generate invoice at /wsfe/invoices")

    sale_data = sale_data.model_dump()
    invoice_result = await request_invoice_controller(sale_data)

    return invoice_result


@router.post("/wsfe/FECompUltimoAutorizado")
async def last_authorized(comp_info: InvoiceBase, jwt = Depends(verify_token)) -> dict:

    logger.info("Received request to fetch last authorized invoice at /wsfe/invoices/last-authorized")

    comp_info = comp_info.model_dump()
    last_authorized_info = await get_last_authorized_info(comp_info)

    return last_authorized_info


@router.post("/wsfe/FECompConsultar")
async def consult_invoice(comp_info: InvoiceQueryRequest, jwt = Depends(verify_token)) -> dict:

    logger.info("Received request to query specific invoice at /wsfe/invoices/query")

    comp_info = comp_info.model_dump()
    result = await consult_specific_invoice(comp_info)

    return result