from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Asserions
import allure


@allure.epic("User registration cases")
class TestUserRegistration(BaseCase):
    @allure.description("Test of creating user with existing email")
    @allure.title("Creating with existing email")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_data_for_client(email)
        response = MyRequests.post("/user/", data=data)
        Asserions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Response contect is wrong. Actual contect is: '{response.content}'"

    @allure.description("Test of creating new user")
    @allure.title("Creating new user")
    def test_create_user(self):
        data = self.prepare_data_for_client()
        response = MyRequests.post('/user', data=data)
        Asserions.assert_code_status(response, 200)
        Asserions.assert_json_has_key(response, 'id')
