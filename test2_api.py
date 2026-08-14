#Фикстуры

import pytest
import requests

#Объявляем фикстуру
@pytest.fixture
def user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response


#Этот тест поменяем  с помощью фикстуры
def test_user_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200


#на
def test_user_status_code(user):  #пишем название фикстуры и проверку
    assert user.status_code == 200



#Этот тест поменяем  с помощью фикстуры
def test_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    assert data[ "id"] == 1
    assert data[ "name"] == "Leanne Graham"


#на

def test_user_data(user):   #пишем название фикстуры и проверку
    data = user.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"



#Этот тест поменяем  с помощью фикстуры
def test_user_email():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    data = response.json()

    assert "@" in data["email"]

#на

def test_user_email(user):   #пишем название фикстуры и проверку
    data = user.json()

    assert "@" in data["email"]


