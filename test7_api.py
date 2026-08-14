#Негативный POST

# с помощью принта нужно получить данные, чтоб понять, какие негативные тесты можно создать, если нет требований
import requests
#
# def test_create_invalid_user():
#     data = {
#         "name": "",
#         "username": "",
#         "email": "wrong-email"
#     }
#
#     response = requests.post(
#         "https://jsonplaceholder.typicode.com/users",
#         json=data
#     )
#
#     print(response.status_code)
#     print(response.json())
#


def test_create_invalid_user():
    data = {
        "name": "",
        "username": "",
        "email": "wrong-email"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=data
    )

    assert response.status_code == 201
