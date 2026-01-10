import pytest
from httpx import AsyncClient

SOAP_RESPONSE = """<?xml version="1.0" encoding="utf-8"?>
<soap-env:Envelope
    xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ar="http://ar.gov.afip.dif.FEV1/">

    <soap-env:Header/>

    <soap-env:Body>
        <ar:FECompUltimoAutorizadoResponse>
            <ar:FECompUltimoAutorizadoResult>
                <ar:PtoVta>1</ar:PtoVta>
                <ar:CbteTipo>6</ar:CbteTipo>
                <ar:CbteNro>1548</ar:CbteNro>
            </ar:FECompUltimoAutorizadoResult>
        </ar:FECompUltimoAutorizadoResponse>
    </soap-env:Body>

</soap-env:Envelope>
"""


@pytest.mark.asyncio
async def test_consult_last_authorized_minimal(client: AsyncClient, httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        SOAP_RESPONSE, content_type="text/xml"
    )

    # Payload
    payload = {
        "Cuit": 30740253022,
        "PtoVta": 1,
        "CbteTipo": 6
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/invoices/last-authorized", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"