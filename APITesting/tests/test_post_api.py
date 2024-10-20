import requests

from APITesting.utiles.utiles import baseUrl

url = baseUrl + 'api/users'

header = {
    'Content-Type': 'application/json; charset=utf-8'
}

payload = {
    "name": "morpheus",
    "job": "leader"
}


def test_post_api():
    response = requests.post(url, headers=header, json=payload)
    print(response.status_code)
    print(response.text)

    r = response.json()
    _id = r['id']

    assert response.status_code == 201
    assert r['name'] == payload['name']

