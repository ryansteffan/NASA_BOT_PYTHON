class NasaApiDataNotFoundError(Exception):
    """
    Represents an exception caused by data not being found in a NASA API
    request.
    """

    def __init__(self, message="The NASA API wrapper has encountered an error"):
        """
        Creates an instance of the NasaApiDataNotFoundError class.

        Args:
            message (str): The message that the exception raises.
        """
        super().__init__(message)
