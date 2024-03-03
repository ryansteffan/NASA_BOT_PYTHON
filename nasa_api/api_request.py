from requests import get


class ApiRequest:

    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint
        self._request_data = get(endpoint).json()

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value: str) -> None:
        self._endpoint = value
        self._request_data = get(value).json()

    @property
    def request_data(self) -> dict:
        return self._request_data
