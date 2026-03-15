import pytest
from httpx import AsyncClient

from tests.integration.soap_responses import (FECAEAConsultarResponse,
                             FECAEASinMovimientoInformarResponse,
                             FEParamGetActividadesResponse,
                             FEParamGetCondicionIvaReceptorResponse,
                             FEParamGetCotizacionResponse,
                             FEParamGetPtosVentaResponse,
                             FEParamGetTiposCbteResponse,
                             FEParamGetTiposConceptoResponse,
                             FEParamGetTiposDocResponse,
                             FEParamGetTiposIvaResponse,
                             FEParamGetTiposMonedasResponse,
                             FEParamGetTiposOpcionalResponse,
                             FEParamGetTiposPaisesResponse,
                             FEParamGetTiposTributosResponse)


@pytest.mark.asyncio
async def test_fecaea_sin_movimiento_informar_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECAEASinMovimientoInformarResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "PtoVta": 1,
        "CAEA": "00000000000000",
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEASinMovimientoInformar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fecaea_consultar_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FECAEAConsultarResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "Periodo": 202603,
        "Orden": 1
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FECAEAConsultar", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_cotizacion_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetCotizacionResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        },
        "MonId" : "DOL"
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetCotizacion", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_tributos_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposTributosResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposTributos", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_monedas_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposMonedasResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposMonedas", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_iva_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposIvaResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposIva", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_opcional_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposOpcionalResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposOpcional", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_concepto_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposConceptoResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposConcepto", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_ptos_venta_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetPtosVentaResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetPtosVenta", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_cbte_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposCbteResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposCbte", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_condicion_iva_receptor_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetCondicionIvaReceptorResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetCondicionIvaReceptor", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_doc_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposDocResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposDoc", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_tipos_paises_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetTiposPaisesResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetTiposPaises", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"


@pytest.mark.asyncio
async def test_fe_param_get_actividades_success(client: AsyncClient, wsfe_httpserver_fixed_port, wsfe_manager, override_auth):

    # Configure http server
    wsfe_httpserver_fixed_port.expect_request("/soap", method="POST").respond_with_data(
        FEParamGetActividadesResponse, content_type="text/xml"
    )

    # Payload
    payload = {
        "Auth": {
            "Cuit": 30740253022
        }
    }

    # Fastapi endpoint call
    resp = await client.post("/wsfe/FEParamGetActividades", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    print(data)
    assert data["status"] == "success"