import requests

baseUrl = "https://reqres.in/"

def get_url():
    return baseUrl

class APIClinet:
    BASE_URL = "https://jsonplaceholder.typicode.com/"
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response