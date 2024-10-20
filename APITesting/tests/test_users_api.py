import pytest

from APITesting.utiles.utiles import APIClinet


@pytest.fixture(scope="module")
def api_client():
    return APIClinet()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0