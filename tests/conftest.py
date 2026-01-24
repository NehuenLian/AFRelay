import datetime
import logging
from pathlib import Path

import pytest
import pytest_asyncio
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from httpx import AsyncClient
from pytest_httpserver import HTTPServer

from config.paths import AfipPaths
from service.api.app import app
from service.soap_client.async_client import WSFEClientManager, wsaa_client
from service.utils.jwt_validator import verify_token

# Zeep logs for debugging
# logging.getLogger("zeep").setLevel(logging.DEBUG)
# logging.getLogger("zeep.transports").setLevel(logging.DEBUG)
# logging.getLogger("zeep.client").setLevel(logging.DEBUG)
# logging.getLogger("zeep.wsdl").setLevel(logging.DEBUG)


# Avoid endpoint Depends=verify_jwt() verification
@pytest.fixture
def override_auth():

    async def fake_verify():
        return {"user" : "test-user", "roles" : ["test"]}
    
    app.dependency_overrides[verify_token] = fake_verify
    yield
    app.dependency_overrides.pop(verify_token, None)


# Use test paths for mock xml files
@pytest.fixture
def afip_paths():
    mocks = Path(__file__).parent / "mocks"
    return AfipPaths(
        base_xml=mocks,
        base_crypto=mocks,
        base_certs=mocks,
    )


# Patch the paths
@pytest.fixture(autouse=True)
def override_afip_paths(afip_paths, monkeypatch):
    monkeypatch.setattr("config.paths.get_afip_paths", lambda: afip_paths)


# Create FastAPI testing client
@pytest.fixture
def client() -> AsyncClient:
    return AsyncClient(app=app, base_url="http://test")


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


# Initialize zeep async client for wsaa with mock wsdl 
# only if httpserver is started
@pytest_asyncio.fixture
def wsaa_manager(wsaa_httpserver_fixed_port):
    mock_path = Path("tests") / "mocks" / "wsfe_mock.wsdl"
    afip_wsdl = str(mock_path.resolve())
    manager = wsaa_client(afip_wsdl)
    yield manager


# Initialize zeep async client with mock wsdl 
# only if httpserver is started
@pytest_asyncio.fixture
async def wsfe_manager(wsfe_httpserver_fixed_port):
    WSFEClientManager.reset_singleton()

    mock_path = Path("tests") / "mocks" / "wsfe_mock.wsdl"
    afip_wsdl = str(mock_path.resolve())
    manager = WSFEClientManager(afip_wsdl)
    yield manager
    await manager.close()

    WSFEClientManager.reset_singleton()


# Generate a fake private key, cert and xml 
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