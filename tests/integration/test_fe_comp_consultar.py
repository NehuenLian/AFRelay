import pytest
from httpx import AsyncClient

SOAP_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <FECompConsultarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECompConsultarResult>
                <ResultGet>
                    <Concepto>1</Concepto>
                    <DocTipo>80</DocTipo>
                    <DocNro>20123456789</DocNro>
                    <CbteDesde>100</CbteDesde>
                    <CbteHasta>100</CbteHasta>
                    <CbteFch>20260109</CbteFch>
                    <ImpTotal>100.00</ImpTotal>
                    <ImpTotConc>0.00</ImpTotConc>
                    <ImpNeto>100.00</ImpNeto>
                    <ImpOpEx>0.00</ImpOpEx>
                    <ImpTrib>0.00</ImpTrib>
                    <ImpIVA>21.00</ImpIVA>
                    <MonId>PES</MonId>
                    <MonCotiz>1.000</MonCotiz>
                    
                    <Resultado>A</Resultado>
                    <CodAutorizacion>74123456789012</CodAutorizacion>
                    <EmisionTipo>CAE</EmisionTipo>
                    <FchVto>20260119</FchVto>
                    <FchProceso>20260109120000</FchProceso>
                    
                    <PtoVta>1</PtoVta>
                    <CbteTipo>6</CbteTipo>
                </ResultGet>
                </FECompConsultarResult>
        </FECompConsultarResponse>
    </soap:Body>
</soap:Envelope>
"""


@pytest.mark.asyncio
async def test_consult_invoice_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        SOAP_RESPONSE, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "FeCompConsReq": {
            "PtoVta": 1,
            "CbteTipo": 6,
            "CbteNro": 100,
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECompConsultar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


# Generic error only for test the API behavior in error cases. Exceptions are already tested in unit tests.
@pytest.mark.asyncio
async def test_consult_invoice_error(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

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
        },
        "FeCompConsReq": {
            "PtoVta": 1,
            "CbteTipo": 6,
            "CbteNro": 100,
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECompConsultar", json=payload)

    assert resp.status_code == 200 # 200 its for FastAPI endpoint
    data = resp.json()
    assert data["status"] == "error"
    assert data["error"]["error_type"] == "HTTP Error"