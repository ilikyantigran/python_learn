from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Asserions
import allure
import pytest

@allure.epic("Authorisation cases")
class TestUserAuth(BaseCase):
    condition = [
        "no_cookie",
        "no_token"
    ]

    def setup_method(self):
        users = {"email": "vinkotov@example.com",
                 "password": "1234"}

        response1 = MyRequests.post("/user/login", data=users)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.x_csrf_token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_value(response1, "user_id")

    @allure.description("Test user auth by email and password")
    @allure.title("Authorisation positive")
    def test_auth_user(self):
        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.x_csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )
        Asserions.assert_json_value_by_name(response2, "user_id", self.user_id,"User_id are not the same")

    @allure.description("Test user auth without sending cookie and token")
    @allure.title("Authorisation negative")
    @pytest.mark.parametrize("condition", condition)
    def test_negative_auth_user(self, condition):
        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.x_csrf_token}
            )
        elif condition == "no_token":
            response2 = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
        Asserions.assert_json_value_by_name(response2, "user_id", 0,f"user has been authorized with condition {condition}")
