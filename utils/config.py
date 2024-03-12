import os.path
from collections import deque

import yaml


class Config:
    """
    Represents a config file and it's contents
    """

    def __init__(self, path: str = "./conf/config.yaml") -> None:
        """
        Creates an instance of the Config class.

        Args:
            path (str): The path to the config file.
        """
        try:
            self._file_path = os.path.abspath(path)
            with open(path) as file:
                self._config_data = yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The Path provided is not valid.")

    @property
    def file_path(self) -> str:
        """
        Gets the config file's file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, value: str) -> None:
        """
        Sets the value of the file path and updates the config being opened.

        Args:
            value (str): The path to the config file being set.
        """
        try:
            self._file_path = os.path.abspath(value)
            with open(value) as file:
                self._config_data = yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The Path provided is not valid.")

    @property
    def config_data(self) -> dict:
        """
        Gets all the config data from the config file.
        """
        return self._config_data

    def get_unique_item(self, index: str) -> str | int | float | list | dict:
        """
        Returns the value of a unique item in the config file

        Args:
            index (str): The name of the item being looked for in the config.

        Raises:
            AttributeError: Is raised when the index value
            is not found in the config file

        Returns:
            str | int | float | list | dict: The value of the specified item.
        """
        queue = deque([self.config_data])

        while queue:
            data = queue.popleft()
            for key, value in data.items():
                if str(key) == index:
                    return value
                elif isinstance(value, dict):
                    queue.append(value)

        raise AttributeError(f"{index} is not in the config file.")

    def update_unique_item(self, index: str,
                           new_value: str | int | float | list) -> None:
        """
        Updates the value of a unique item in the config file.

        Args:
            index (str): The name of the item being looked for in the config.
            new_value (str | int | float | list): The new value that the item
            in the config file is being set to.

        Raises:
            AttributeError: Is raised when the value could not be set due the
            item not existing in the config.
        """
        is_success = False
        queue = deque([self.config_data.copy()])

        while queue:
            data = queue.popleft()
            for key, value in data.items():
                if str(key) == index:
                    data[key] = new_value
                    with open(self.file_path, 'w') as file:
                        yaml.safe_dump(self.config_data, file)
                    is_success = True
                elif isinstance(value, dict):
                    queue.append(value)

        if not is_success:
            raise AttributeError(
                f"Value could not be set. Ensure that {index} is in the "
                f"config file.")
