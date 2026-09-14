#POST Запрос

import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#
#
# print(response.status_code)
# print(response.json())




def test_create_user():
    data = {
        "name": "Tatyana",
        "username": "Lilia",
        "email": "tatyana@example.com"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=data
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == "Tatyana"
    assert response_data["email"] == "tatyana@example.com"
    assert response_data()["username"] == "Liliia"




