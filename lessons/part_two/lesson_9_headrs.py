import requests


headers = {"some_header": "123"}

response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
# здесь мы получим ответ сервера в формате текста json, здесь указаны какие заголовки сервер получил от клиента
print(response.text)
# здесь мы получили от сервера на запрос
print(response.headers)
