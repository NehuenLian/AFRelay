from unittest.mock import MagicMock, patch

import httpx
import pytest

from tests.test_wsaa.mocks.xml_mocks import loginCmsResponse


@pytest.mark.asyncio
async def test_login_cms_success(
                                    client: httpx.AsyncClient, 
                                    wsaa_httpserver_fixed_port, 
                                    patch_request_access_token_dependencies,
                                    override_auth
                                ):

    # Configure http server
    wsaa_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        loginCmsResponse, content_type="text/xml"
    )

    # Magic mocks patched directly in the test for practicality
    xml_saver_mock = MagicMock()
    parse_and_save_loginticketresponse_mock = MagicMock()
    with patch("src.wsaa.controllers.request_access_token_controller.save_xml", xml_saver_mock):
        with patch("src.wsaa.controllers.request_access_token_controller.parse_and_save_loginticketresponse", parse_and_save_loginticketresponse_mock):
                  
            resp = await client.post("/wsaa/loginCms")

    assert resp.status_code == 200
    data = resp.json()

    assert data["status"] == "success"
    assert xml_saver_mock.call_count == 1
    assert parse_and_save_loginticketresponse_mock.call_count == 1


# Generic error only for test the API behavior in error cases. Exceptions are already tested in unit tests.
@pytest.mark.asyncio
async def test_login_cms_error(
                                    client: httpx.AsyncClient, 
                                    wsaa_httpserver_fixed_port, 
                                    patch_request_access_token_dependencies,
                                    override_auth
                                ):

    # Configure http server
    wsaa_httpserver_fixed_port.expect_request("/not_existent", method="POST").respond_with_data(
        "Internal Server Error",
        status=500,
        content_type="text/plain",
    )

    # Magic mocks patched directly in the test for practicality
    xml_saver_mock = MagicMock()
    parse_and_save_loginticketresponse_mock = MagicMock()
    with patch("src.wsaa.controllers.request_access_token_controller.save_xml", xml_saver_mock):
        with patch("src.wsaa.controllers.request_access_token_controller.parse_and_save_loginticketresponse", parse_and_save_loginticketresponse_mock):
                  
            resp = await client.post("/wsaa/loginCms")

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "error generating access token."