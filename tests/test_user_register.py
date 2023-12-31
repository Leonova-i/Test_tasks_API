import allure
import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions


class TestUserRegister(BC):
    def test_create_successfully(self):
        data = self.prepare_register_data()

        response_register = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_register_data(email)

        response_register = MyRequests.post('user/', data=data)

        Assertions.assert_status_code(response_register, 400)
        assert response_register.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected content'{response_register.content}'"

    @allure.story("Ira tests")
    def test_create_user_without_at(self):
        data = self.prepare_register_data_without_at()
        response = MyRequests.post('user/', data=data)

        Assertions.assert_status_code(response, 400), f"Unexpected status code '{response.status_code}'. " \
                                                      f"User hasn't '@' in  email."

    @allure.story("Ira tests")
    def test_create_user_with_short_name(self):
        data = self.prepare_register_data_with_short_name()

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400), f"Unexpected status code '{response.status_code}'. " \
                                                      f"User has short name"

    @allure.story("Ira tests")
    def test_create_user_with_very_long_name(self):
        data = self.prepare_register_data_with_very_long_name()

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400), f"Unexpected status code '{response.status_code}'. " \
                                                      f"User has very long name"

    @allure.story("Ira tests")
    @pytest.mark.parametrize("password, username",
                             [("qwerty@example.com", ""),
                              ("", "Max"),
                              ("", "")])
    def test_create_user_with_parametrize(self, password, username):
        data = {'password': password,
                'username': username,
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': 'mail_for_negative_check'
                }

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_status_code(response, 400), f"Unexpected status code '{response.status_code}'. " \
                                                      f"User has very long name"
