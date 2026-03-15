import pytest
from httpx import AsyncClient

from tests.integration.soap_responses import FECompTotXRequestResponse


@pytest.mark.asyncio
async def test_fe_comp_tot_x_request(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECompTotXRequestResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECompTotXRequest", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


# Generic error only for test the API behavior in error cases. Exceptions are already tested in unit tests.
@pytest.mark.asyncio
async def test_fe_comp_tot_x_error(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/not_existent", method="POST").respond_with_data(
        "Internal Server Error",
        status=500,
        content_type="text/plain",
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECompTotXRequest", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["error"]["error_type"] == "HTTP Error"