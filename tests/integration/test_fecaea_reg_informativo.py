import pytest
from httpx import AsyncClient

from tests.integration.soap_responses import FECAEARegInformativoResponse


@pytest.mark.asyncio
async def test_fecaea_reg_informativo_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECAEARegInformativoResponse, content_type="text/xml"
    )

    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "FeCAEARegInfReq": {
            "FeCabReq": {
                "CantReg": 1,
                "PtoVta": 1,
                "CbteTipo": 1
            },
            "FeDetReq": {
                "FECAEADetRequest": [
                    {
                        "Concepto": 1,
                        "DocTipo": 99,
                        "DocNro": 20123456789,
                        "CbteDesde": 1,
                        "CbteHasta": 1,
                        "CbteFch": "20260125",
                        "ImpTotal": 121.00,
                        "ImpTotConc": 0.00,
                        "ImpNeto": 100.00,
                        "ImpOpEx": 0.00,
                        "ImpIVA": 21.00,
                        "ImpTrib": 0.00,
                        "MonId": "PES",
                        "MonCotiz": 1.00,
                        "CondicionIVAReceptorId": 1,
                        "CAEA": "12345678901234"
                    }
                ]
            }
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEARegInformativo", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


# Generic error only for test the API behavior in error cases. Exceptions are already tested in unit tests.
@pytest.mark.asyncio
async def test_fecaea_reg_informativo_error(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/not_existent", method="POST").respond_with_data(
        FECAEARegInformativoResponse, content_type="text/xml"
    )

    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "FeCAEARegInfReq": {
            "FeCabReq": {
                "CantReg": 1,
                "PtoVta": 1,
                "CbteTipo": 1
            },
            "FeDetReq": {
                "FECAEADetRequest": [
                    {
                        "Concepto": 1,
                        "DocTipo": 99,
                        "DocNro": 20123456789,
                        "CbteDesde": 1,
                        "CbteHasta": 1,
                        "CbteFch": "20260125",
                        "ImpTotal": 121.00,
                        "ImpTotConc": 0.00,
                        "ImpNeto": 100.00,
                        "ImpOpEx": 0.00,
                        "ImpIVA": 21.00,
                        "ImpTrib": 0.00,
                        "MonId": "PES",
                        "MonCotiz": 1.00,
                        "CondicionIVAReceptorId": 1,
                        "CAEA": "12345678901234"
                    }
                ]
            }
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEARegInformativo", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["error"]["error_type"] == "HTTP Error"