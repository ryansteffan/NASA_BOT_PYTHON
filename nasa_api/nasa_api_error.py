class NasaApiDataNotFound(Exception):
    def __init__(self, message="The NASA API wrapper has encountered an error"):
        super().__init__(message)
