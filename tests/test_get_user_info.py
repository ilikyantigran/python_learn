import allure

from lib.base_case import BaseCase
from lib.assertions import Asserions
from lib.my_requests import MyRequests


@allure.epic("Test cases of getting info about user")
class TestGetUserInfo(BaseCase):
    @allure.description("Test of getting info about authorized user")
    @allure.title("Get User (authorized)")
    def test_get_user_authorized(self):
        user = {"email": "vinkotov@example.com",
                "password": "1234"}

        response1 = MyRequests.post("/user/login", data=user)
        cookie = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": cookie})
        fields = [
            "username",
            "email",
            "firstName",
            "lastName"
        ]
        Asserions.assert_json_has_keys(response2, fields)

    @allure.description("Test of getting info about unauthorized user")
    @allure.title("Get User (unauthorized)")
    def test_get_user_not_authorized(self):
        response = MyRequests.get('/user/2')
        fields = [
            "email",
            "firstName",
            "lastName"
        ]
        Asserions.assert_json_has_key(response, "username")
        Asserions.assert_json_does_not_have_keys(response, fields)