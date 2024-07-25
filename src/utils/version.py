class Version:

    def __init__(self, version_file: str) -> None:
        self._version_file = version_file
        self._version = self._get_version()

    @property
    def version_file(self):
        return self._version_file

    @version_file.setter
    def version_file(self, value):
        self._version_file = value
        self._version = self._get_version()

    @property
    def version(self):
        return self._version

    def is_most_recent(self):
        ...

    def _get_version(self):
        with open(self._version_file, "r") as file:
            self._version = file.read()

    def _get_remote_commit_hashes(self):
        ...
