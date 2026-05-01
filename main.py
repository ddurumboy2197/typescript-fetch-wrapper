import requests

class FetchWrapper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str, params: dict = None) -> dict:
        url = f"{self.base_url}{path}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, data: dict) -> dict:
        url = f"{self.base_url}{path}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, path: str, data: dict) -> dict:
        url = f"{self.base_url}{path}"
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, path: str) -> dict:
        url = f"{self.base_url}{path}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()
