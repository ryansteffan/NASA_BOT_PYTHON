import requests

from src.nasa_api.api_request import ApiRequest
from src.nasa_api.nasa_api_errors import NasaApiDataNotFoundError


class Apod(ApiRequest):
    """
    Represents a request to the APOD NASA API.
    """

    def __init__(self, endpoint: str) -> None:
        """
        Cerates an instance of the Apod class.

        Args:
            endpoint (str): The apod endpoint.
        """
        super().__init__(endpoint)

    @property
    def copyright(self) -> str:
        """
        Copy right info for the request.

        Returns
            str: The copy right info for the request.

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not have
                                      copyright info.
        """
        try:
            return super().request_data["copyright"]
        except KeyError:
            raise NasaApiDataNotFoundError(
                "Request did not contain copyright info.")

    @property
    def date(self) -> str:
        """
        The date that corresponds to the Astronomy Picture of the Day date.

        Returns:
            str: The request APOD date.

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not have a
                                      date.
        """
        try:
            return super().request_data["date"]
        except KeyError:
            raise NasaApiDataNotFoundError("Request did not contain a date.")

    @property
    def explanation(self) -> str:
        """
        An explanation of the image/video that is in the request.

        Returns:
            str: The explanation for the image/video in the request.

        Raises:
            NasaApiDataNotFoundError: Raised when an explanation is not found
                                      in the request.
        """
        try:
            return super().request_data["explanation"]
        except KeyError:
            raise NasaApiDataNotFoundError(
                "Request did not contain an explanation.")

    @property
    def media_type(self) -> str:
        """
        The type of media that the requests contains. Should be an image or
        video.

        Returns:
            str: The type of media in the request.

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not have a
                                      media type.
        """
        try:
            return super().request_data["media_type"]
        except KeyError:
            raise NasaApiDataNotFoundError(
                "Request did not contain a media_type.")

    @property
    def service_version(self) -> str:
        """
        The version of the system that provides the API.

        Returns:
            str: The version of the service that provides the API.

        Raises:
            NasaApiDataNotFoundError: Raised when a service version is not in
                                      the response.
        """
        try:
            return super().request_data["service_version"]
        except KeyError:
            raise NasaApiDataNotFoundError("Request did not contain a service "
                                           "version.")

    @property
    def title(self) -> str:
        """
        The title of the image/video in the request.

        Returns:
            str: The title of the image/video in the request.

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not
                                      contain a title.
        """
        try:
            return super().request_data["title"]
        except KeyError:
            raise NasaApiDataNotFoundError("Request did not contain a title.")

    @property
    def url(self) -> str:
        """
        The URL that points the image/video of the day.

        Returns:
            str: The URL that points to the image/video of the day.

        Raises:
            NasaApiDataNotFoundError: Is raised when the request does not
                                      contain a URL.
        """
        try:
            return super().request_data["url"]
        except KeyError:
            raise NasaApiDataNotFoundError("Request did not contain a url.")

    @property
    def hdurl(self) -> str:
        """
        The URL that links to an HD version of the image in the request.

        Returns:
            str: The URL that links to the HD version of the image in the
                 request.

        Raises:
            NasaApiDataNotFoundError: Is raised if the request does not
                                      contain an HD URL (hdurl in request).
        """
        try:
            return super().request_data["hdurl"]
        except KeyError:
            raise NasaApiDataNotFoundError(
                "Request data did not contain an hdurl. Check if "
                "request has provided a video.")

    def is_video(self) -> bool:
        """
        Checks if the content of the request is a video.

        Returns:
            bool: Returns true if the content is a video.
        """
        return self.media_type == "video"

    def is_image(self) -> bool:
        """
        Checks if the content of the request is an image.

        Returns:
            str: Returns true of the content is an image.
        """
        return self.media_type == "image"

    def download_image(self, file_path: str) -> None:
        """
        Downloads the image from the URL to the specified file path.

        Args:
            file_path (str): The path where the image will be saved.

        Returns: None

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not return
            a status code of 200 or if the request does not contain an image.
        """
        if self.is_image():
            with open(file_path, 'wb') as file:
                response = requests.get(self.url)
                if response.status_code == 200:
                    file.write(response.content)
                else:
                    raise NasaApiDataNotFoundError(
                        f"Failed to download image. Status code: "
                        f"{response.status_code}")
        else:
            raise NasaApiDataNotFoundError("Request does not contain an image.")

    def download_hd_image(self, file_path: str) -> None:
        """
        Downloads the HD image from the URL to the specified file path.

        Args:
            file_path (str): The path where the HD image will be saved.

        Returns: None

        Raises:
            NasaApiDataNotFoundError: Raised when the request does not return
            a status code of 200 or if the request does not contain an image.
        """
        if self.is_image():
            with open(file_path, 'wb') as file:
                response = requests.get(self.hdurl)
                if response.status_code == 200:
                    file.write(response.content)
                else:
                    raise NasaApiDataNotFoundError(
                        f"Failed to download HD image. Status code: "
                        f"{response.status_code}")
        else:
            raise NasaApiDataNotFoundError("Request does not contain an image.")
