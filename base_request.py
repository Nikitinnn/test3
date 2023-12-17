import requests

class BaseApi:
    base_url = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, json=data, params=params)
        response.raise_for_status()
        return response.json()
