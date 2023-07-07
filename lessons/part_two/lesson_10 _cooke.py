import requests

# # # ######## получаем куки  ############
# # # переменная для передачи параметров
# # payload = {"login": "secret_login", "password": "secret_pass"}
# # response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# #
# # print(response.text)
# # print(response.status_code)
# # # объект cookie
# # print(response.cookies)
# # # объект cookie в dict
# # print(dict(response.cookies))
#
#
# # ######## передаем куки в последующий запрос  ############
# # отправляем запрос с предварительно составленными данными в payload
# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# # из переменной response1 получаем данные cookie  "auth_cookie" и кладем эти значения в переменную cookie_value
# cookie_value = response1.cookies.get("auth_cookie")
# # создаем словарь для авторизованного cookie
# cookies = {"auth_cookie": cookie_value}
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
# #  печатаем тест ответа
# print(response2.text)


# ######## обработка на случай пустых cookie ############


payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)


cookie_value = response1.cookies.get("auth_cookie")
# создаем пустой массив
cookies = {}
if cookie_value is not None:
    # добавляем cookie_value только если она сущ-ет
    cookies.update({"auth_cookie": cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
#  печатаем тест ответа
print(response2.text)
