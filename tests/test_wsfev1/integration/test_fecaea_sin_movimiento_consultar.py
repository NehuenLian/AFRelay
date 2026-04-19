import pytest
from httpx import AsyncClient

from tests.test_wsfev1.mocks.soap_responses import \
    FECAEASinMovimientoConsultarResponse


@pytest.mark.asyncio
async def test_fecaea_sin_movimiento_consultar_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECAEASinMovimientoConsultarResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "CAEA": "00000000000000",
        "PtoVta": 1
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfev1/FECAEASinMovimientoConsultar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success" # TODO: Update assertion once WSDL inconsistencies are resolved; currently expecting 'error'.