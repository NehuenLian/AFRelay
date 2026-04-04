from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.shared.api.jwt_validator import verify_token
from src.shared.api.response_models.errors import APIErrorResponseModel
from src.shared.utils.logger import logger
from src.wsaa.controllers.request_access_token_controller import \
    generate_afip_access_token


class loginCmsResponse(BaseModel):
    status: str

router = APIRouter()

@router.post("/wsaa/loginCms", response_model=loginCmsResponse | APIErrorResponseModel)
async def renew_access_token(jwt = Depends(verify_token)) -> dict:
    
    logger.info("Received request to generate access token at /wsaa/loginCms")

    response_status = await generate_afip_access_token()

    return response_status