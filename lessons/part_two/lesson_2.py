import requests

# переменная для передачи параметров
paylod = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=paylod)

print(response.text)


response = requests.get("https://playground.learnqa.ru/api/hello")

print(response.text)
