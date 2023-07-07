import requests

# проверка типа запроса
response = requests.get("https://playground.learnqa.ru/api/check_type")
print(response.text)

# проверка типа запроса
response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.text)

# проверка типа запроса
response = requests.put("https://playground.learnqa.ru/api/check_type")
print(response.text)

# проверка типа запроса
response = requests.delete("https://playground.learnqa.ru/api/check_type")
print(response.text)
