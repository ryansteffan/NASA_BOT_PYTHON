from unittest import TestCase

import responses

from nasa_api.api_request import ApiRequest


class TestApiRequest(TestCase):
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
    def test_init_endpoint_is_set(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data

        # Act
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="application/json"
        )

        target = ApiRequest(endpoint)
        actual = target._endpoint

        # Assert
        expected = endpoint
        self.assertEqual(actual, expected)

    @responses.activate
    def test_init_request_data_is_pulled_from_api(self):
        # Arrange
        endpoint = self.image_endpoint
        api_data = self.image_request_data

        # Act
        responses.add(
            responses.GET,
            url=endpoint,
            json=api_data,
            status=200,
            content_type="applications/json"
        )
        target = ApiRequest(endpoint)
        actual = target._request_data

        # Assert
        expected = api_data
        self.assertEqual(actual, expected)

    @responses.activate
    def test_endpoint_get_value(self):
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
        target = ApiRequest(endpoint)

        # Act
        actual = target.endpoint

        # Assert
        expected = endpoint
        self.assertEqual(actual, expected)

    @responses.activate
    def test_endpoint_endpoint_is_set(self):
        # Arrange
        original_endpoint = self.image_endpoint
        original_api_data = self.image_request_data
        new_endpoint = self.video_endpoint
        new_api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=original_endpoint,
            json=original_api_data,
            status=200,
            content_type="application/json"
        )
        responses.add(
            responses.GET,
            url=new_endpoint,
            json=new_api_data,
            status=200,
            content_type="application/json"
        )
        target = ApiRequest(original_endpoint)

        # Act
        target.endpoint = new_endpoint
        actual = target._endpoint

        # Assert
        expected = new_endpoint
        self.assertEqual(actual, expected)

    @responses.activate
    def test_endpoint_request_data_is_updated(self):
        # Arrange
        original_endpoint = self.image_endpoint
        original_api_data = self.image_request_data
        new_endpoint = self.video_endpoint
        new_api_data = self.video_request_data
        responses.add(
            responses.GET,
            url=original_endpoint,
            json=original_api_data,
            status=200,
            content_type="application/json"
        )
        responses.add(
            responses.GET,
            url=new_endpoint,
            json=new_api_data,
            status=200,
            content_type="application/json"
        )
        target = ApiRequest(original_endpoint)

        # Act
        target.endpoint = new_endpoint
        actual = target._request_data

        # Assert
        expected = new_api_data
        self.assertEqual(actual, expected)

    @responses.activate
    def test_response_data_get_value(self):
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
        target = ApiRequest(endpoint)

        # Act
        actual = target.request_data

        # Assert
        expected = api_data
        self.assertEqual(actual, expected)
