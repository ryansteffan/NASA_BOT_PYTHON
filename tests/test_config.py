import os.path
import tempfile
from unittest import TestCase
from unittest.mock import patch, mock_open

from src.utils import Config


class TestConfig(TestCase):
    # Used when mocking a file has unintended side effects.
    # Such as trying to assert a FileNotFoundError with a mock.
    temp_dir = tempfile.TemporaryDirectory(dir=".", suffix="_temp")
    test_file = tempfile.NamedTemporaryFile(suffix=".yaml", delete=False,
                                            dir=temp_dir.name)
    test_file_path = test_file.name
    test_file.close()

    def test_init_invalid_file_path_set(self):
        # Arrange
        file_path = "Not a real file path"

        # Act
        with self.assertRaises(FileNotFoundError) as context:
            Config(file_path)

        # Assert
        expected = "The Path provided is not valid."
        self.assertEqual(str(context.exception), expected)

    def test_init_check_if_attributes_are_set_correctly(self):
        # Arrange
        file_path = "test.yaml"
        file_data = "test: value"

        # Act
        with patch('builtins.open', mock_open(read_data=file_data)):
            target = Config(file_path)
            actual_path = target._file_path
            actual_data = target._config_data

        # Assert
        expected_path = os.path.abspath("test.yaml")
        expected_data = {"test": "value"}
        self.assertEqual(actual_path, expected_path)
        self.assertEqual(actual_data, expected_data)

    def test_file_path_get_value(self):
        # Arrange
        file_path = "test.yaml"
        file_data = "test: value"

        # Act
        with patch("builtins.open", mock_open(read_data=file_data)):
            target = Config(file_path)
            actual = target.file_path

        # Assert
        expected = os.path.abspath("test.yaml")
        self.assertEqual(actual, expected)

    def test_file_path_invalid_path_set(self):
        # Arrange
        fake_file_path = "This is not a real file path"
        target = Config(self.test_file_path)

        # Act
        with self.assertRaises(FileNotFoundError) as context:
            target.file_path = fake_file_path

        # Assert
        expected = "The Path provided is not valid."
        self.assertEqual(str(context.exception), expected)

    def test_config_data_get_value(self):
        # Arrange
        file_path = "test.yaml"
        file_data = "test: value"

        # Act
        with patch("builtins.open", mock_open(read_data=file_data)):
            target = Config(file_path)
            actual = target.config_data

        # Assert
        expected = {"test": "value"}
        self.assertEqual(actual, expected)

    def test_get_unique_item_value_not_in_config_file(self):
        # Arrange
        file_path = "test.yaml"
        file_data = "test: value"
        lookup_value = "Fake item"

        # Act
        with patch("builtins.open", mock_open(read_data=file_data)):
            target = Config(file_path)
            with self.assertRaises(AttributeError) as context:
                target.get_unique_item(lookup_value)

        # Assert
        expected = "Fake item is not in the config file."
        self.assertEqual(str(context.exception), expected)

    def test_get_unique_item_returns_correct_data(self):
        # Arrange
        file_path = "test.yaml"
        file_data = """
                    root:
                        item1: value1
                        layer2:
                            item2: value2
                    """
        lookup_value = "item2"

        # Act
        with patch("builtins.open", mock_open(read_data=file_data)):
            target = Config(file_path)
            actual = target.get_unique_item(lookup_value)

        # Assert
        expected = "value2"
        self.assertEqual(actual, expected)

    def test_update_unique_item_value_not_in_config_file(self):
        # Arrange
        file_path = "test.yaml"
        file_data = """
                    root:
                        item1: value1
                        layer2:
                            item2: value2
                    """
        lookup_value = "Fake item"
        new_value = "New value"

        # Act
        with patch("builtins.open", mock_open(read_data=file_data)):
            target = Config(file_path)
            with self.assertRaises(AttributeError) as context:
                target.update_unique_item(lookup_value, new_value)

        # Assert
        expected = ("Value could not be set. Ensure that Fake item is in the "
                    "config file.")
        self.assertEqual(str(context.exception), expected)

    def test_update_unique_item_value_is_written(self):
        # Arrange
        file_path = "test.yaml"
        file_data = """
                    root:
                        item1: value1
                        layer2:
                            item2: value2
                    """
        lookup_value = "item2"
        new_value = "New value"

        # Act
        with ((patch("builtins.open", mock_open(read_data=file_data))) as
              mocked_file):
            target = Config(file_path)
            target.update_unique_item(lookup_value, new_value)

        # Assert
        self.assertEqual(mocked_file.call_count, 2)

    # Used to ensure there is no copy errors.
    def test_update_unique_item_two_values_are_updated_and_written(self):
        # Arrange
        file_path = "test.yaml"
        file_data = """
                    root:
                        item1: value1
                        layer2:
                            item2: value2
                    """
        lookup_value_one = "item1"
        new_value_one = "newValue1"
        lookup_value_two = "item2"
        new_value_two = "newValue2"

        # Act
        with ((patch("builtins.open", mock_open(read_data=file_data))) as
              mocked_file):
            target = Config(file_path)
            target.update_unique_item(lookup_value_one, new_value_one)
            target.update_unique_item(lookup_value_two, new_value_two)

        # Assert
        self.assertEqual(mocked_file.call_count, 3)
