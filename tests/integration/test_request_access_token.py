from pathlib import Path
from unittest.mock import MagicMock, patch

import httpx
import pytest
from zeep import AsyncClient
from zeep.transports import AsyncTransport

from ..conftest import generate_test_files

SOAP_RESPONSE = """<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://wsaa.view.sua.dvadac.desein.afip.gov">
   <soapenv:Body>
      <ns1:loginCmsResponse>
         <ns1:loginCmsReturn><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<loginTicketResponse version="1.0">
    <header>
        <source>CN=wsaahomo, O=AFIP, C=AR, SERIALNUMBER=CUIT 33693450239</source>
        <destination>SERIALNUMBER=CUIT 30740253022, CN=certificadodefinitivo</destination>
        <uniqueId>3634574819</uniqueId>
        <generationTime>2026-01-07T02:40:09.235-03:00</generationTime>
        <expirationTime>2026-01-07T14:40:09.235-03:00</expirationTime>
    </header>
    <credentials>
        <token>fake_token</token>
        <sign>fake_sign</sign>
    </credentials>
</loginTicketResponse>]]>
         </ns1:loginCmsReturn>
      </ns1:loginCmsResponse>
   </soapenv:Body>
</soapenv:Envelope>
"""

@pytest.mark.asyncio
async def test_generate_afip_access_token_success(client: AsyncClient, wsaa_httpserver_fixed_port, wsaa_manager, override_auth):
    
    def fake_time_provider():
        return (
            1767764408,
            "2026-01-07T05:40:08Z",
            "2026-01-07T05:50:08Z",
        )

    def fake_wsdl_manager():
        mock_path = Path("tests") / "mocks" / "wsaa_mock.wsdl"
        afip_wsdl = str(mock_path.resolve())
        return afip_wsdl
    
    def wsaa_client_mock(afip_wsdl):

        httpx_client = httpx.AsyncClient(timeout=30.0)
        transport = AsyncTransport(client=httpx_client)
        client = AsyncClient(wsdl=afip_wsdl, transport=transport)

        return client, httpx_client

    # Configure http server
    wsaa_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        SOAP_RESPONSE, content_type="text/xml"
    )

    xml_saver_mock = MagicMock()

    with patch("service.controllers.request_access_token_controller.get_wsaa_wsdl", fake_wsdl_manager):
        with patch("service.controllers.request_access_token_controller.wsaa_client", wsaa_client_mock):
            with patch("service.controllers.request_access_token_controller.generate_ntp_timestamp", fake_time_provider):
                with patch("service.controllers.request_access_token_controller.save_xml", xml_saver_mock):
                    with patch("service.controllers.request_access_token_controller.get_as_bytes", generate_test_files):
                        with patch("service.controllers.request_access_token_controller.parse_and_save_loginticketresponse", MagicMock()):
                                        
                            resp = await client.post("/wsaa/token")

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    assert xml_saver_mock.call_count == 1