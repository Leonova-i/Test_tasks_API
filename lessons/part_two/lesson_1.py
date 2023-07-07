import requests

# in variable(переменная) keep in itself(хранит в себе) response to a request (ответ на запрос)здесь хранится
# информация об ответе на запрос
# также мы импортируем библиотеку requests
response = requests.get("https://playground.learnqa.ru/api/hello")
# распечатывает текст ответа(json в котором будет содержаться приветственная строка)
print(response.text)

# Задача 1
# Представим, что мы тестируем форму авторизации на любом веб-сайте.
# Пользователь должен заполнить email, пароль и отправить форму. Соответственно,
# в момент отправки сформируется и отправится HTTP-запрос. Какой тип запроса вы бы ожидали увидеть в этом случае:
# GET или POST? Почему?




