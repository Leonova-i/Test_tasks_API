from lib.my_requests import MyRequests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions
import allure


class TestUserDelete(BC):
    @allure.story("Ira tests")
    def test_get_user_negative_delete(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response1, 200)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_json_has_key(response2, 'firstName')

        response3 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response3, 400)
        assert response3.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    @allure.story("Ira tests")
    def test_get_user_delete(self):
        data_login = self.prepare_register_data()
        email = data_login['email']
        password = data_login['password']

        data = {
            'email': email,
            'password': password
        }

        response = MyRequests.post('user/', data=data_login)
        Assertions.assert_status_code(response, 200)

        response1 = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response1, 200)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_json_has_key(response2, 'firstName')

        response3 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response3, 200)

