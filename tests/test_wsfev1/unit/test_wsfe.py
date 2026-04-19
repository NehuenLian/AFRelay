import httpx
import pytest
from unittest.mock import AsyncMock, MagicMock

from src.wsfev1.soap_client.wsfev1 import consult_afip_wsfev1

fake_xml = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <message>mock test</message>
        <id>123</id>
    <soap:Body>
</root>
"""

fake_xml_response = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <Result>approved</Result>
    </soap:Body>
</soap:Envelope>
"""

# ===== Success =======
@pytest.mark.asyncio
async def test_consult_afip_wsfe_success():

    mock_response = MagicMock()
    mock_response.text = fake_xml_response
    mock_client = AsyncMock()
    mock_client.post.return_value = mock_response

    response = await consult_afip_wsfev1(fake_xml, "TestMethod", client=mock_client)

    assert response["status"] == "success"
# ====================


# ===== Errors =======
@pytest.mark.asyncio
async def test_consult_afip_wsfe_http_status_error():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)
    m_response = MagicMock(spec=httpx.Response)

    error_real = httpx.HTTPStatusError(
        "HTTP Error",
        request=m_request,
        response=m_response
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsfev1(fake_xml, "TestMethod", client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "HTTP Error"


@pytest.mark.asyncio
async def test_consult_afip_wsfe_connect_error():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)

    error_real = httpx.ConnectError(
        "Network error",
        request=m_request,
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsfev1(fake_xml, "TestMethod", client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "Network error"


@pytest.mark.asyncio
async def test_consult_afip_wsfe_timeout():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)

    error_real = httpx.TimeoutException(
        "Timeout Error",
        request=m_request,
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsfev1(fake_xml, "TestMethod", client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "Network error"


@pytest.mark.asyncio
async def test_consult_afip_wsfe_unknown_error():

    mock_client = AsyncMock()
    mock_client.post.side_effect = Exception

    response = await consult_afip_wsfev1(fake_xml, "TestMethod", client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "unknown"
