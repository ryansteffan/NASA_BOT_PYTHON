from nasa_api.api_request import ApiRequest
from nasa_api.nasa_api_error import NasaApiDataNotFound


class Apod(ApiRequest):
    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint)

    @property
    def copyright(self):
        try:
            return super().request_data["copyright"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain copyright info.")

    @property
    def date(self):
        try:
            return super().request_data["date"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain a date.")

    @property
    def explanation(self):
        try:
            return super().request_data["explanation"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain an explanation.")

    @property
    def media_type(self):
        try:
            return super().request_data["media_type"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain a media_type.")

    @property
    def service_version(self):
        try:
            return super().request_data["service_version"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain a service "
                                      "version.")

    @property
    def title(self):
        try:
            return super().request_data["title"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain a title.")

    @property
    def url(self):
        try:
            return super().request_data["url"]
        except KeyError:
            raise NasaApiDataNotFound("Request did not contain a url.")

    @property
    def hdurl(self):
        try:
            return super().request_data["hdurl"]
        except KeyError:
            raise NasaApiDataNotFound(
                "Request data does not contain an hdurl. Check if "
                "request has provided a video.")

    def is_video(self) -> bool:
        return self.media_type == "video"

    def is_image(self) -> bool:
        return self.media_type == "image"
