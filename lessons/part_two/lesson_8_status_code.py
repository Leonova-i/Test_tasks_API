import requests

# успешно
response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)


# рассмотрим с ошибкой и попробуем получить и статус код и текст
response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)
# Текста нет, т.к. сервер не обработал запрос не в штатном режиме


# рассмотрим с несуществующим методом something
response = requests.post("https://playground.learnqa.ru/api/something")
print(response.status_code)
print(response.text)
# Ошибка несуществующего метода 404 и тест ответа, т. к. переходя по несуществующему url мы получаем
# отрисованную страницу, содержащую html и является полноценной страницей

# ######## метод allow_redirects False #############
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)


# ######### метод allow_redirects #############
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# Узнаем историю перенаправления. Фун-я history возвращаем массив всех ответов, которые мы получили прежде чем,
# оказались на итоговом url
first_response = response.history[0]
# перекладываем для наглядности в second_response
second_response = response

print(first_response.url)
print(second_response.url)
print(response.status_code)  # ресурс запрещен для клиента, а мог быть ответ 200


response = requests.get("https://playground.learnqa.ru/")
print(response.status_code)
