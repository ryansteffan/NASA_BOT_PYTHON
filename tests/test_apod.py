from unittest import TestCase

import responses

from nasa_api.apod import Apod
from nasa_api.nasa_api_errors import NasaApiDataNotFoundError


class TestApod(TestCase):
    # Data below is used to mock the format that is expected from an APOD
    # request to the NASA API
    image_endpoint = "http://test.local/api/image"
    image_request_data = {
        "copyright": "Stefano De Rosa",
        "date": "2010-01-01",
        "explanation": "This bright Full Moon was captured on December 2nd, "
                       "shining above a church overlooking the River Po, "
                       "in Turin, Italy. It was the first Full Moon in "
                       "December. Shining on celebrations of New Year's Eve, "
                       "last night's Full Moon was the second Full Moon of "
                       "December and so fits the modern definition of a Blue "
                       "Moon - the second Full Moon in a month. Because the "
                       "lunar cycle, Full Moon to Full Moon, spans 29.5 days, "
                       "Blue Moons tend to occur in some month about every "
                       "2.5 years. Shining in the glare just above and right "
                       "of December's first Full Moon is the Pleiades star "
                       "cluster.",
        "hdurl": "https://apod.nasa.gov/apod/image/1001"
                 "/NBMoon_StefanoDeRosa_lg.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Not a Blue Moon",
        "url": "https://apod.nasa.gov/apod/image/1001/NBMoon_StefanoDeRosa_sm"
               ".jpg"
    }

    video_endpoint = "http://test.local/api/video"
    video_request_data = {
        "copyright": "\nJun Ho Oh (KAIST, \nHuboLab); \n Music: \nFlowing Air "
                     "by \nMattia Vlad Morleo\n",
        "date": "2024-03-03",
        "explanation": "How would you feel if the Sun disappeared? Many "
                       "eclipse watchers across the USA surprised themselves "
                       "in 2017 with the awe that they felt and the "
                       "exclamations that they made as the Sun momentarily "
                       "disappeared behind the Moon. Perhaps expecting just a "
                       "brief moment of dusk, the spectacle of unusually "
                       "rapid darkness, breathtakingly bright glowing beads "
                       "around the Moon's edge, shockingly pink solar "
                       "prominences, and a strangely detailed corona "
                       "stretching across the sky caught many a curmudgeon by "
                       "surprise.  Many of these attributes  were captured in "
                       "the featured real-time, three-minute video of 2017's "
                       "total solar eclipse. The video frames were acquired "
                       "in  Warm Springs, Oregon with equipment specifically "
                       "designed by Jun Ho Oh to track a close-up of the "
                       "Sun's periphery during eclipse.  As the video ends, "
                       "the Sun is seen being reborn on the other side of the "
                       "Moon from where it departed.  Next month, on April "
                       "8th, a new total solar eclipse will be visible in a "
                       "thin band across North America.",
        "media_type": "video",
        "service_version": "v1",
        "title": "A Total Solar Eclipse Close-Up in Real Time",
        "url": "https://www.youtube.com/embed/5D9j-8Vhyto?rel=0&showinfo=0"
    }

    @responses.activate
    def test_init_image_endpoint_is_set(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )

        # Act
        target = Apod(endpoint)
        actual = target._endpoint

        # Assert
        expected = endpoint
        self.assertEqual(actual, expected)

    @responses.activate
    def test_init_video_endpoint_is_set(self):
        # Arrange
        endpoint = self.video_endpoint
        api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )

        # Act
        target = Apod(endpoint)
        actual = target._endpoint

        # Assert
        expected = endpoint
        self.assertEqual(actual, expected)

    @responses.activate
    def test_init_image_request_data_is_pulled_from_api(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )

        # Act
        target = Apod(endpoint)
        actual = target._request_data

        # Assert
        expected = api_data
        self.assertEqual(actual, expected)

    @responses.activate
    def test_init_video_request_data_is_pulled_from_api(self):
        # Arrange
        endpoint = self.video_endpoint
        api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )

        # Act
        target = Apod(endpoint)
        actual = target._request_data

        # Assert
        expected = api_data
        self.assertEqual(actual, expected)

    @responses.activate
    def test_copyright_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["copyright"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.copyright

        # Assert
        expected = "Request did not contain copyright info."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_copyright_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.copyright

        # Assert
        expected = api_data["copyright"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_date_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["date"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.date

        # Assert
        expected = "Request did not contain a date."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_date__gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.date

        # Assert
        expected = api_data["date"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_explanation_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["explanation"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.explanation

        # Assert
        expected = "Request did not contain an explanation."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_explanation_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.explanation

        # Assert
        expected = api_data["explanation"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_media_type_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["media_type"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.media_type

        # Assert
        expected = "Request did not contain a media_type."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_media_type_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.media_type

        # Assert
        expected = api_data["media_type"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_service_version_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["service_version"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.service_version

        # Assert
        expected = "Request did not contain a service version."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_service_version_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.service_version

        # Assert
        expected = api_data["service_version"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_title_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["title"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.title

        # Assert
        expected = "Request did not contain a title."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_title_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.title

        # Assert
        expected = api_data["title"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_url_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        del api_data["url"]
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.url

        # Assert
        expected = "Request did not contain a url."
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_url_gets_value(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.url

        # Assert
        expected = api_data["url"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_hdurl_raises_NasaApiDataNotFoundError(self):
        # Arrange
        endpoint = self.video_endpoint
        api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        with self.assertRaises(NasaApiDataNotFoundError) as context:
            actual = target.hdurl

        # Assert
        expected = ("Request data did not contain an hdurl. Check if request "
                    "has provided a video.")
        self.assertEqual(str(context.exception), expected)

    @responses.activate
    def test_hdurl_gets_value_from_image_request(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.hdurl

        # Assert
        expected = api_data["hdurl"]
        self.assertEqual(actual, expected)

    @responses.activate
    def test_is_video_returns_true_for_video_request(self):
        # Arrange
        endpoint = self.video_endpoint
        api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.is_video()

        # Assert
        expected = True
        self.assertEqual(actual, expected)

    @responses.activate
    def test_is_video_returns_false_for_image_request(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.is_video()

        # Assert
        expected = False
        self.assertEqual(actual, expected)

    @responses.activate
    def test_is_image_returns_true_for_image_request(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.is_image()

        # Assert
        expected = True
        self.assertEqual(actual, expected)

    @responses.activate
    def test_is_image_returns_false_for_video_request(self):
        # Arrange
        endpoint = self.video_endpoint
        api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )
        target = Apod(endpoint)

        # Act
        actual = target.is_image()

        # Assert
        expected = False
        self.assertEqual(actual, expected)
