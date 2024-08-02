import os.path
import subprocess

class Version:

    def __init__(self, version_file: str, remote_url: str) -> None:
        self._version_file = os.path.abspath(version_file)
        self._remote_url = remote_url
        with open(self.version_file, "r") as file:
            self._version = file.readline()

    @property
    def version(self):
        return self._version

    @property
    def version_file(self):
        return self._version_file

    @property
    def remote_url(self):
        return self._remote_url

    def is_most_recent(self):
        hashes = self._get_remote_commit_hashes().values()
        version_names = self._get_remote_commit_hashes().keys()
        version = self.version
        for hash in hashes:
            if version == hash:
                return True
        return False

    def get_most_recent_stable_version(self):
        ...

    def get_most_recent_rolling_version(self):
        ...

    def _get_remote_commit_hashes(self) -> dict:
        version_hashes = {}
        delimited_remote_hashes = subprocess.getoutput(
            f"git ls-remote {self.remote_url}")
        delimited_remote_hashes = delimited_remote_hashes.replace("\t", ":")
        branch_name = ""
        lines = []
        for character in delimited_remote_hashes:
            if character == "\n":
                lines.append(branch_name)
                branch_name = ""
            if character != "\n":
                branch_name += character
        lines.append(branch_name)

        for line in lines:
            items = line.split(":")
            hash, branch_name = items[0], items[1]
            reversed_branch_name = branch_name[::-1]

            version = ""

            do_reorder = True
            iteration_counter = 0
            while do_reorder and iteration_counter != len(reversed_branch_name):
                character = reversed_branch_name[iteration_counter]
                if character == "/":
                    do_reorder = False
                elif character != "/":
                    version += character
                iteration_counter += 1

            version_hashes[version[::-1]] = hash

        return version_hashes
