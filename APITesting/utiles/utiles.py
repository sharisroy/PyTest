import requests

baseUrl = "https://reqres.in/api/"

def get_url():
    return baseUrl

class APIClinet:
    BASE_URL = "https://reqres.in/api/"
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, payload):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    def patch(self, endpoint, payload):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.patch(url, headers=self.headers, json=payload)
        return response


class Person:
    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def set_id(self, _id):
        self.id = _id
        print(_id)
    def set_name(self, _name):
        self.name = _name
        print(_name)

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name




