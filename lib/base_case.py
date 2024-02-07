from datetime import datetime
from requests import Response
import json


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can not find cookie with name '{cookie_name}'"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Can not find header with name '{header_name}'"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError :
            assert False, f"Response is not in json format. Response text is '{response.text}'"

        assert name in response_as_dict, f"There is no '{name}' in the response"
        return response_as_dict[name]

    def prepare_data_for_client(self, email = None):
        if email is None:
            base_part = "test"
            domain = "example.com"
            random_part = datetime.now().strftime("%Y%m%d%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            "username": "123",
            "firstName": "123",
            "lastName": "123",
            "email": email,
            "password": "123"
        }
