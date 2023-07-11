import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions
import allure


class TestUserEdit(BC):

    def test_edit_just_create_user(self):
        register_date = self.prepare_register_data()
        response_register = MyRequests.post('user/', data=register_date)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_date["email"]
        password = register_date['password']
        user_id = self.get_json_value(response_register, 'id')

        login_data = {
            'email': email,
            'password': password
        }

        response_login = MyRequests.post('user/login', data=login_data)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, "x-csrf-token")

        new_name = "Changed name"
        response_put = MyRequests.put(f'user/{user_id}',
                                      cookies={'auth_sid': auth_sid},
                                      headers={"x-csrf-token": token},
                                      data={'firstName': new_name})
        Assertions.assert_status_code(response_put, 200)

        response_check_put = MyRequests.get(f'user/{user_id}',
                                            cookies={'auth_sid': auth_sid},
                                            headers={"x-csrf-token": token})

        Assertions.assert_json_value_by_name(
            response_check_put,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    @allure.story("Ira tests")
    def test_edit_just_create_user_without_at(self):

        register_date = self.prepare_register_data()
        data_for_email = self.prepare_register_data_without_at()
        email_without_at = data_for_email["email"]
        email = register_date["email"]
        password = register_date['password']
        login_data_for_check = {'email': email, 'password': password}

        response_create = MyRequests.post('user/', data=register_date)
        Assertions.assert_status_code(response_create, 200)

        user_id = self.get_json_value(response_create, 'id')

        response_login = MyRequests.post('user/login', data=login_data_for_check)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, "x-csrf-token")

        response_check_changes = MyRequests.put(f'user/{user_id}',
                                                cookies={'auth_sid': auth_sid},
                                                headers={"x-csrf-token": token},
                                                data={'email': email_without_at})

        Assertions.assert_status_code(response_check_changes, 400)
        assert response_check_changes.text == "Invalid email format"

    @allure.story("Ira tests")
    def test_edit_change_short_name(self):
        register_date = self.prepare_register_data()
        email = register_date["email"]
        password = register_date['password']
        login_data_for_check = {'email': email, 'password': password}

        response_create = MyRequests.post('user/', data=register_date)

        Assertions.assert_status_code(response_create, 200)
        user_id = self.get_json_value(response_create, 'id')

        response_login = MyRequests.post('user/login', data=login_data_for_check)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, "x-csrf-token")

        response_check_changes = MyRequests.put(f'user/{user_id}',
                                                cookies={'auth_sid': auth_sid},
                                                headers={"x-csrf-token": token},
                                                data={'firstName': "i"})

        Assertions.assert_status_code(response_check_changes, 400)
        assert response_check_changes.text == '{"error":"Too short value for field firstName"}'
        Assertions.assert_json_has_key(response_check_changes, "error")

    @allure.story("Ira tests")
    def test_edit_changes_without_auth(self):
        response_check_changes = MyRequests.put(f'user/2', data={'firstName': "someName"})

        Assertions.assert_status_code(response_check_changes, 400)
        assert response_check_changes.text == "Auth token not supplied"

    @allure.story("Ira tests")
    def test_edit_changes_with_auth_another_user(self):
        register_date = self.prepare_register_data()
        email = register_date["email"]
        password = register_date['password']
        login_data_for_check = {'email': email, 'password': password}

        response_create = MyRequests.post('user/', data=register_date)

        Assertions.assert_status_code(response_create, 200)

        MyRequests.post('user/login', data=login_data_for_check)

        response_check_changes = MyRequests.put(f'user/2', data={'firstName': "someName"})

        Assertions.assert_status_code(response_check_changes, 400)
        assert response_check_changes.text == "Auth token not supplied"
