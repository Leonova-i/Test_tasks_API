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

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_files = ["username", 'firstName', 'lastName', 'email']
        Assertions.assert_json_has_keys(response2, expected_files)

    @allure.story("Ira tests")
    def test_with_auth_user_and_check_another_user(self):
        data ={
            'email': 'qwerty@qwerty.com',
            'password': '12345'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_files = ["username", 'firstName', 'lastName', 'email']
        Assertions.assert_json_has_keys(response2, expected_files)

        response3 = MyRequests.get('user/2')
        print("******", response3.json(), "*************")

        Assertions.assert_json_has_key(response3, "username")
        Assertions.assert_json_has_not_key(response3, 'firstName')
        Assertions.assert_json_has_not_key(response3, 'lastName')
        Assertions.assert_json_has_not_key(response3, 'email')
