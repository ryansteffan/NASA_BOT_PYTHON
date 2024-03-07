from requests import get


class ApiRequest:
    """
    Represents a request to a NASA API
    """

    def __init__(self, endpoint: str) -> None:
        """
        Creates an instance of the ApiRequest class.

        Args:
            endpoint (str): The endpoint url for the request.
        """
        self._endpoint = endpoint
        self._request_data = get(endpoint).json()

    @property
    def endpoint(self) -> str:
        """
        Gets the endpoint url for the request.
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value: str) -> None:
        """
        Sets the endpoint for the request and updates the request data.

        Args:
            value (str): The new endpoint url
        """
        self._endpoint = value
        self._request_data = get(value).json()

    @property
    def request_data(self) -> dict:
        """
        Gets the request data from the request made the endpoint.
        """
        return self._request_data
