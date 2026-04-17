import datetime
from pathlib import Path
from unittest.mock import patch

import httpx
import pytest
import pytest_asyncio
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from pytest_httpserver import HTTPServer

from src.shared.api.jwt_validator import verify_token
from src.shared.main import app
from src.shared.paths_config.paths import AfipPaths
from src.wsfev1.soap_client.client_manager import WSFEClientManager


# Avoid endpoint Depends=verify_jwt() verification (all features)
@pytest.fixture 
def override_auth():

    async def fake_verify():
        return {"user" : "test-user", "roles" : ["test"]}
    
    app.dependency_overrides[verify_token] = fake_verify
    yield
    app.dependency_overrides.pop(verify_token, None)


# Use test paths for mock xml files (all features)
@pytest.fixture
def afip_paths():
    mocks = Path(__file__).parent / "test_shared" / "mocks"
    return AfipPaths(
        base_xml=mocks,
        base_crypto=mocks,
        base_certs=mocks,
    )


# Patch the paths (all features)
@pytest.fixture(autouse=True)
def override_afip_paths(afip_paths, monkeypatch):
    monkeypatch.setattr("src.shared.paths_config.paths.get_afip_paths", lambda: afip_paths)


# Create FastAPI testing client (all features)
@pytest.fixture
def client() -> httpx.AsyncClient:
    return httpx.AsyncClient(app=app, base_url="http://test")


# Force http server at 62768 for wsfe
@pytest.fixture
def wsfe_httpserver_fixed_port():
    server = HTTPServer(port=62768)
    server.start()
    yield server
    server.stop()


# Force http server at 23592 for wsaa
@pytest.fixture
def wsaa_httpserver_fixed_port():
    server = HTTPServer(port=23592)
    server.start()
    yield server
    server.stop()


# Initialize zeep async client for wsfe
# only if httpserver is up
@pytest_asyncio.fixture
async def wsfe_manager(wsfe_httpserver_fixed_port):
    WSFEClientManager.reset_singleton()

    manager = WSFEClientManager()
    yield manager
    await manager.close()

    WSFEClientManager.reset_singleton()


# Patch server url with fake http server for wsfev1 service. (wsfe)
@pytest.fixture
def patch_url_wsfev1_dependencies():

    def wsfev1_client_mock():
        return "http://localhost:62768/soap"

    with patch("src.wsfev1.soap_client.wsfev1.get_wsfe_url", wsfev1_client_mock):
        yield


# Patch functions with fakes for request_access_token_controller integration test. (wsaa)
@pytest.fixture
def patch_request_access_token_dependencies():

    def fake_time_provider():
        return (
            1767764408,
            "2026-01-07T05:40:08Z",
            "2026-01-07T05:50:08Z",
        )

    def wsaa_client_mock():
        return "http://localhost:23592/soap"

    with patch("src.wsaa.controllers.request_access_token_controller.generate_ntp_timestamp", fake_time_provider):
        with patch("src.wsaa.controllers.request_access_token_controller.get_as_bytes", generate_test_files):
            with patch("src.wsaa.soap_client.wsaa.get_wsaa_url", wsaa_client_mock):
                yield


# Generate a fake private key, cert and xml (wsaa)
# for testing access token processes
def generate_test_files() -> tuple[bytes, bytes, bytes]:

    # Create private key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    # ===

    # Create certificate
    subject = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Test"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Test City")
    ])
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(subject)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1))
        .sign(private_key, hashes.SHA256())
    )
    cert_bytes_pem = cert.public_bytes(serialization.Encoding.PEM)
    # ===

    # Create XML
    login_ticket_request = """<?xml version='1.0' encoding='UTF-8'?>
    <loginTicketRequest>
    <header>
        <uniqueId>1767764408</uniqueId>
        <generationTime>2026-01-07T05:40:08Z</generationTime>
        <expirationTime>2026-01-07T05:50:08Z</expirationTime>
    </header>
    <service>wsfe</service>
    </loginTicketRequest>
    """
    xml_bytes = login_ticket_request.encode('utf-8')
    # ===

    return xml_bytes, private_key_bytes, cert_bytes_pem