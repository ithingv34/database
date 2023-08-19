import pytest

from starlette.testclient import TestClient

from src.server import app


@pytest.fixture(scope="module")
def anyio_backend():
    """Module fixture."""

    return "asyncio"


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as test_client:
        yield test_client
