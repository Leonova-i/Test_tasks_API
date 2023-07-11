import pytest
from lib.base_case import BaseCase as BC
from lib.assertions import Assertions
from lib.my_requests import MyRequests


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

        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")

    def test_auth_user(self):
        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})

        # 3 вызова заменили одним
        Assertions.assert_json_value_by_name(
            response_auth,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

    @pytest.mark.parametrize("condition", params_for_check)
    def test_negative_check_user(self, condition):
        if condition == "non_cookies":
            response_check = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token})
        else:
            response_check = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response_check,
            "user_id",
            0,
            f"User is authorize auth in the response with {condition}"
        )
