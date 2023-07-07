import json
import random
from datetime import datetime

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find cookie with name {headers_name} in the last response"
        return response.headers[headers_name]

    # Проверяем ответ в формате json. парсим ответ
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        # если парсинг прошел успешно, то возвращаем name
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_register_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{randon_part}@{domain}"
        return {'password': "123",
                'username': "learnqa",
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': email
                }

    def prepare_register_data_without_at(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{randon_part}{domain}"
        return {'password': "123",
                'username': "learnqa",
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': email
                }

    def prepare_register_data_with_short_name(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{randon_part}{domain}"
            name_user = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm'))])

        return {'password': "123",
                'username': name_user,
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': email
                }

    def prepare_register_data_with_very_long_name(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{randon_part}{domain}"
            name_user = (''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCV'))
                         for _ in range(250)]))

        return {'password': "123",
                'username': name_user,
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': email
                }

    def prepare_register_data_without_password(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            randon_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{randon_part}@{domain}"
        return {'password': None,
                'username': "learnqa",
                'firstName': "learnqa",
                'lastName': "learnqa",
                'email': email
                }
