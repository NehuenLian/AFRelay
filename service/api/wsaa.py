from fastapi import APIRouter, Depends

from service.controllers.request_access_token_controller import \
    generate_afip_access_token
from service.utils.jwt_validator import verify_token
from service.utils.logger import logger

router = APIRouter()

@router.post("/wsaa/loginCms")
async def renew_access_token(jwt = Depends(verify_token)) -> dict:
    
    logger.info("Received request to generate invoice at /wsfe/invoices")

    response_status = await generate_afip_access_token()

    return response_status