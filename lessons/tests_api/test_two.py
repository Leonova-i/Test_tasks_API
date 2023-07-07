import requests
import pytest


class TestFirstAPI:
    names = [
        ("Irina"),
        ("Max"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "'answer' is not in dict"

        if len(name) == 0:
            expect_response_text = f"Hello, someone"
        else:
            expect_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expect_response_text, "Actual text in the response is not correct "
