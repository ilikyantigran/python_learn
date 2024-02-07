from requests import Response
import json


class Asserions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not valid JSON. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not contain key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not a valid JSON. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON does not contain key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not a valid JSON. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON does not contain key '{name}'"

    @staticmethod
    def assert_code_status(response: Response, code):
        assert response.status_code == code, f"Expected code - {code}. Actual code - {response.status_code}"

    @staticmethod
    def assert_json_does_not_have_key(response: Response, key):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not a valid JSON. Response text is '{response}"
        assert key not in response_as_dict, f"Key '{key}' is in response"

    @staticmethod
    def assert_json_does_not_have_keys(response: Response, keys: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not a valid JSON. Response text is '{response}"
        for key in keys:
            assert key not in response_as_dict, f"Key '{key}' is in response"