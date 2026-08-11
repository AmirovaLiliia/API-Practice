# #import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#
# print(response.status_code)
# print(response.json())


import requests

#
# def test_get_user():
#     # 1. Отправить GET-запрос
#     response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#
#     # 2. Проверить, что статус-код равен 200
#     assert response.status_code == 200
#
#     # 3. Получить JSON из ответа
#     data = response.json()
#
#     # 4. Проверить, что id пользователя равен 1
#     assert data[ "id" ] == 1
#     #негативный тест
#     # assert data[ "id" ] == 4
#
#
#     #5.Что имя пользователя равно "Leanne Graham"
#     assert data[ "name" ] == "Leanne Graham"
#
#     # негативный тест
#     # assert data[ "name" ] == "Leanne Grah"
#
#
#     #6. Что в email присутствует символ @
#     assert "@" in data["email" ]
#
#
# #Запуск в терминале pytest test1_api.py -v


# Сделать все асерты тремя отдельными тестами


def test_user_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200


def test_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    assert data[ "id" ] == 1
    assert data[ "name" ] == "Leanne Graham"


def test_user_email():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    data = response.json()

    assert "@" in data["email" ]





