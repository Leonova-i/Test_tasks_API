from datetime import datetime

import requests
from lib.base_case import BaseCase as BC
from datetime import datetime
from lib.assertions import Assertions


# class TestUserRegister(BC):
#     def setup(self):
base_part = "learnqa"
domain = "example.com"
randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
email = f'{base_part}{randon_part}@{domain}'
print(email)


    # test_
    # def test_create_successfully(self):
    #     data = {'username': "learnqa",
    #             'firstName': "learnqa",
    #             'lastName': "learnqa",
    #             'email': self.email,
    #             'password': "123"
    #             }
    #
    #     response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
    #
    #     Assertions.assert_status_code(response, 200)
    #     Assertions.assert_json_has_key(response, "id")
    #
    # def test_create_user_with_existing_email(self):
    #     email = 'vinkotov@example.com'
    #     data = {'username': "learnqa",
    #             'firstName': "learnqa",
    #             'lastName': "learnqa",
    #             'email': email,
    #             'password': "123"}
    #
    #     response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
    #     print(response.status_code)
    #     print(response.content)
    #
    #     assert response.status_code == 400, f"Unexpected status code '{response.status_code}'"
    #     assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
    #         f"Unexpected content'{response.content}'"



#
# class TestUserRegister(BC):
#     def test_create_successfully(self):
#         data = self.prepare_register_data()
#
#         response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
#         print(response.status_code)
#
#         Assertions.assert_status_code(response, 200)
#         Assertions.assert_json_has_key(response, "id")
#
#     def test_create_user_with_existing_email(self):
#         email = 'vinkotov@example.com'
#         data = self.prepare_register_data(email)
#
#
#         # data = {'username': "learnqa",
#         #         'firstName': "learnqa",
#         #         'lastName': "learnqa",
#         #         'email': email,
#         #         'password': "123"}
#
#         response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
#         print(response.status_code)
#         print(response.content)
#
#         assert response.status_code == 400, f"Unexpected status code '{response.status_code}'"
#         assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
#             f"Unexpected content'{response.content}'"
