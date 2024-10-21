import pytest
import requests

from APITesting.utiles.utiles import APIClinet, Person


@pytest.fixture(scope="module")
def api_client():
    return APIClinet()

def test_get_users(api_client):
    response = api_client.get("users?page=2")
    print(response.url)
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_user_by_id(api_client):
    response = api_client.get("users/2")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_get_user_not_found(api_client):
    response = api_client.get("unknown/23")
    print(response.json())
    assert response.status_code == 404
    assert len(response.json()) == 0
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

payload = {
    "name": "Haris Chandra Roy",
    "job": "leader"
}

person = Person()
def test_post_create_user(api_client):
    response = api_client.post("users", payload)
    print(response.status_code)
    print(response.text)

    r = response.json()
    _id = r['id']

    person.set_id(_id)
    person.set_name(payload['name'])

    print(person.get_id())
    assert response.status_code == 201
    assert r['name'] == payload['name']



@pytest.mark.skip
def test_get_user_created(api_client):

    response = api_client.get(f"users/{person.get_id()}")
    print(response.url)
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


def test_patch_update_user(api_client):
    response = api_client.patch("users/5", payload)
    print(response.status_code)
    print(response.text)

    r = response.json()
    person.set_name(payload['name'])

    print(person.get_id())
    assert response.status_code == 200
    assert r['name'] == payload['name']

def test_get_user_updated(api_client):

    response = api_client.get(f"users/5")
    print(response.url)
    print(response.json())
    r = response.json()

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

