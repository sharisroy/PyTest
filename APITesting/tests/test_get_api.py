
import requests

from APITesting.utiles.utiles import baseUrl


def test_get_url():
    print(baseUrl)


def test_get_response_data():
    response = requests.get(baseUrl + 'api/users/2')
    print(response.status_code)
    print(response.json())
    r = response.json()
    print(r['data'])
    print(r['data']['id'])
    print(r['data']['email'])
    print(r['data']['first_name'])

    print(r['support'])
    print(r['support']['url'])
    print(r['support']['text'])


    assert response.status_code == 200
    assert r['data']['id'] == 2
    assert r['support']['url'] == "https://reqres.in/#support-heading"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


def test_get_response_headers():
    response = requests.get(baseUrl + 'api/users/2')
    print(response.status_code)
    print(response.headers)
    print(response.headers['Date'])
    print(response.headers['Content-Type'])
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'