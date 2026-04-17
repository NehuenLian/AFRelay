from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from src.wsaa.soap_client.wsaa import consult_afip_wsaa
from tests.test_wsaa.mocks.xml_mocks import loginCms


# ===== Success =======
@pytest.mark.asyncio
async def test_consult_afip_wsaa_success():

    mock_response = MagicMock()
    mock_response.json.return_value = {"status" : "success", "response" : "approved"}

    mock_client = AsyncMock()
    mock_client.post.return_value = mock_response

    response = await consult_afip_wsaa(loginCms, client=mock_client)

    assert response["status"] == "success"
# ====================


# ===== Errors =======
@pytest.mark.asyncio
async def test_consult_afip_wsaa_transport_error():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)
    m_response = MagicMock(spec=httpx.Response)

    error_real = httpx.HTTPStatusError(
        "HTTP Error",
        request=m_request,
        response=m_response
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsaa(loginCms, client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "HTTP Error"


@pytest.mark.asyncio
async def test_consult_afip_wsaa_connection_error():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)

    error_real = httpx.ConnectError(
        "Network error",
        request=m_request,
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsaa(loginCms, client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "Network error"


@pytest.mark.asyncio
async def test_consult_afip_wsaa_timeout():

    mock_client = AsyncMock()
    m_request = MagicMock(spec=httpx.Request)

    error_real = httpx.TimeoutException(
        "Timeout Error",
        request=m_request,
    )

    mock_client.post.side_effect = error_real

    response = await consult_afip_wsaa(loginCms, client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "Network error"


@pytest.mark.asyncio
async def test_consult_afip_wsaa_timeout():

    mock_client = AsyncMock()
    mock_client.post.side_effect = Exception

    response = await consult_afip_wsaa(loginCms, client=mock_client)

    assert response["status"] == "error"
    assert response["error"]["error_type"] == "unknown"
