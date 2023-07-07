import json


# задаем переменную типа str
string_as_json_format = '{"answer": "Hello, User"}'

# с помощью библиотеки json парсим строку и она превращается в объект по св-м как словарь
obj = json.loads(string_as_json_format)
print(obj)
# обращаемся по ключу и возвращаем объект
# ! всегда поверяем наличие вызываемого ключа
print(obj["answer"])

# как проверить:
# выносим чтобы не писаит много раз
# key = "answer"
#
# # проверяем есть ли он
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Ключа {key} в JSON нет")

