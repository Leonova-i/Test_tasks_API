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

        response_login = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response_login, 200)
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response_login, "user_id")

        response_auth = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid})

        Assertions.assert_json_has_key(response_auth, 'firstName')

        response_delete = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                            headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response_delete, 400)
        assert response_delete.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    @allure.story("Ira tests")
    def test_get_user_delete(self):
        data_login = self.prepare_register_data()
        email = data_login['email']
        password = data_login['password']

        data = {
            'email': email,
            'password': password
        }

        response_create = MyRequests.post('user/', data=data_login)
        Assertions.assert_status_code(response_create, 200)

        response_login = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response_login, 200)
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response_login, "user_id")

        response_auth = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                       headers={"x-csrf-token": token},
                                       cookies={"auth_sid": auth_sid})

        Assertions.assert_json_has_key(response_auth, 'firstName')

        response_delete = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                            headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response_delete, 200)
