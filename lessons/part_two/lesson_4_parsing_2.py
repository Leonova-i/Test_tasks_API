import requests
from json.decoder import JSONDecodeError

# парсим через библиотеку request
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# парсим тут
parsed_response_text = response.json()
print(parsed_response_text["answer"])


### ошибочный вариан, если ответ приходит не в формате json. через метод get.test#####

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
# # парсим тут
# parsed_response_text = response.json()
# print(parsed_response_text)
#
# ###### как избежать и словить ошибку  ############


# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
# # парсим тут
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not JSON format")
