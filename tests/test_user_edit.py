import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions
import allure


class TestUserEdit(BC):

    def test_edit_just_create_user(self):
        # Register
        register_date = self.prepare_register_data()

        response1 = MyRequests.post('user/', data=register_date)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_date["email"]
        password = register_date['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post('user/login', data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(f'user/{user_id}',
                                   cookies={'auth_sid': auth_sid},
                                   headers={"x-csrf-token": token},
                                   data={'firstName': new_name})

        Assertions.assert_status_code(response3, 200)

        # GET
        response4 = MyRequests.get(f'user/{user_id}', cookies={'auth_sid': auth_sid}, headers={"x-csrf-token": token})

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )

    @allure.story("Ira tests")
    def test_edit_just_create_user_without_at(self):

        register_date = self.prepare_register_data()
        data_for_email = self.prepare_register_data_without_at()
        email_without_dt_for_check = data_for_email["email"]
        email = register_date["email"]
        password = register_date['password']
        login_data_for_check = {'email': email, 'password': password}

        response_create = MyRequests.post('user/', data=register_date)

        Assertions.assert_status_code(response_create , 200)
        user_id = self.get_json_value(response_create , 'id')

        # LOGIN

        response_login = MyRequests.post('user/login', data=login_data_for_check)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT

        response_fail_change = MyRequests.put(f'user/{user_id}',
                                              cookies={'auth_sid': auth_sid},
                                              headers={"x-csrf-token": token},
                                              data={'email': email_without_dt_for_check})

        Assertions.assert_status_code(response_fail_change, 400)
        assert response_fail_change.text == "Invalid email format"
