import requests
import pytest
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions


class TestUserAuth(BC):
    params_for_check = [
        ("non_cookies"),
        ("non_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")
        # assert "user_id" in response1.json(), "There is no user id in the response"
        # self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})
        # 3 вызова заменили одним
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        # вызовы которых заменили
        # assert "user_id" in response2.json(), "There is no user id in the second response"
        # user_id_from_check_method = response2.json()["user_id"]
        # assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal" \
        #                                                                    " to user id from check method"

    @pytest.mark.parametrize("condition", params_for_check)
    def test_negative_check_user(self, condition):
        if condition == "non_cookies":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorize auth in the response with {condition}"
        )


        # assert "user_id" in response2.json(), "There is no user id in the second response"
        # user_id_from_check_method = response2.json()["user_id"]
        # assert user_id_from_check_method == 0, f"User is authorized auth in the response with {condition}"
