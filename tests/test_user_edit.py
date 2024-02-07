import allure
from lib.base_case import BaseCase
from lib.assertions import Asserions
from lib.my_requests import MyRequests

@allure.epic("Test cases about editing user")
class TestUserEdit(BaseCase):

    @allure.description("Positive case of creating new user, editing his name and checking has it been changed")
    @allure.title("End-to-End case")
    def test_creating_and_editing_user(self):
        # Регистрация
        registration_data = self.prepare_data_for_client()
        response1 = MyRequests.post("/user/", data=registration_data)

        Asserions.assert_code_status(response1, 200)
        Asserions.assert_json_has_key(response1, 'id')

        email = registration_data["email"]
        firstName = registration_data["firstName"]
        password = registration_data["password"]
        user_id = self.get_json_value(response1, "id")

        # Авторизация
        users = {"email": email,
                 "password": password}
        response2 = MyRequests.post("/user/login", data=users)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Изменение
        new_name = "Changed"
        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        Asserions.assert_code_status(response3, 200)

        # Проверка
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Asserions.assert_json_value_by_name(response4, "firstName", new_name,
                                            "Name does not match expected edited name")
