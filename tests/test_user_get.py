from lib.my_requests import MyRequests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions
import allure


class TestUserGet(BC):
    def test_get_user_without_auth(self):
        response = MyRequests.get('user/2')
        print(response.json())

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, 'firstName')
        Assertions.assert_json_has_not_key(response, 'lastName')
        Assertions.assert_json_has_not_key(response, 'email')

    def test_get_user_with_auth_the_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_login = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response_login, "user_id")

        response_het_auth = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                           headers={"x-csrf-token": token},
                                           cookies={"auth_sid": auth_sid})

        expected_files = ["username", 'firstName', 'lastName', 'email']
        Assertions.assert_json_has_keys(response_het_auth, expected_files)

    @allure.story("Ira tests")
    def test_with_auth_user_and_check_another_user(self):
        data = {
            'email': 'qwerty@qwerty.com',
            'password': '12345'
        }

        response_login = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response_login, "user_id")

        response_get_auth = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                           headers={"x-csrf-token": token},
                                           cookies={"auth_sid": auth_sid})

        expected_files = ["username", 'firstName', 'lastName', 'email']
        Assertions.assert_json_has_keys(response_get_auth, expected_files)

        response_check = MyRequests.get('user/2')

        Assertions.assert_json_has_key(response_check, "username")
        Assertions.assert_json_has_not_key(response_check, 'firstName')
        Assertions.assert_json_has_not_key(response_check, 'lastName')
        Assertions.assert_json_has_not_key(response_check, 'email')
