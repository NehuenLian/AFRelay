import pytest
from httpx import AsyncClient

from tests.integration.soap_responses import FECAEASolicitarResponse


@pytest.mark.asyncio
async def test_fecaea_solicitar_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECAEASolicitarResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "Periodo": 202602,
        "Orden": 1
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEASolicitar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


# Generic error only for test the API behavior in error cases. Exceptions are already tested in unit tests.
@pytest.mark.asyncio
async def test_fecaea_solicitar_error(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/not_existent", method="POST").respond_with_data(
        FECAEASolicitarResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "Periodo": 202602,
        "Orden": 1
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEASolicitar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["error"]["error_type"] == "HTTP Error"