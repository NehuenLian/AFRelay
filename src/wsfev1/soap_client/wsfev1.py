import logging
from builtins import ConnectionResetError

import httpx
from tenacity import (before_sleep_log, retry, retry_if_exception_type,
                      stop_after_attempt, wait_fixed)

from src.shared.utils.logger import logger
from src.shared.utils.response_management import (build_error_response,
                                                  clear_response)
from src.wsfev1.soap_client.client_manager import WSFEClientManager
from src.wsfev1.soap_client.url_manager import get_wsfe_url


def consult_afip_wsfe():
    pass

@retry(
        retry=retry_if_exception_type(( ConnectionResetError, httpx.ConnectError )),
        stop=stop_after_attempt(3),
        wait=wait_fixed(0.5),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )
async def consult_afip_wsfev1(xml_string, METHOD: str,  client=None) -> dict:

    if client is None:
        manager = WSFEClientManager()
        client = manager.get_client()

    url = get_wsfe_url()
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': f"http://ar.gov.afip.dif.FEV1/{METHOD}"
    }
    print(f"xml_string: {xml_string}")
    try:
        response = await client.post(url, content=xml_string, headers=headers)
        print(f"response: {response}")
        response.raise_for_status()
        cleaned_response = clear_response(response)
        print(f"cleaned_response: {cleaned_response}")
        return {
            "status" : "success",
            "response" : cleaned_response
        }

    except httpx.HTTPStatusError as e:
        return build_error_response(METHOD, "HTTP Error", str(e))

    except (httpx.ConnectError, httpx.TimeoutException) as e:
        return build_error_response(METHOD, "Network error", str(e))

    except Exception as e:
        logger.error(f"General exception in {METHOD}: {e}")
        return build_error_response(METHOD, "unknown", str(e))
