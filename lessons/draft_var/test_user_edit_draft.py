import requests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions


class TestUserEdit(BC):
    def test_edit_just_create_user(self):
        # Register
        register_date = self.prepare_register_data()

        response1 = requests.post('https://playground.learnqa.ru/api/user/', data=register_date)
        print(response1.status_code)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        # раскладываем соответсвующее данные для будущих запросов
        email = register_date["email"]
        first_name = register_date["firstName"]
        password = register_date['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = requests.put(f'https://playground.learnqa.ru/api/user/{user_id}',
                                 cookies={'auth_sid': auth_sid},
                                 headers={"x-csrf-token": token},
                                 data={'firstName': new_name})

        Assertions.assert_status_code(response3, 200)

        # GET
        response4 = requests.get(f'https://playground.learnqa.ru/api/user/{user_id}',
                                 cookies={'auth_sid': auth_sid},
                                 headers={"x-csrf-token": token})

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
