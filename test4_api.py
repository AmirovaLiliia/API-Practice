# PUT Запрос


import requests
def test_update_user():
    data = {
        "name": "Tatyana Updated",
        "email": "updated@example.com"
    }
    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=data
    )

    assert response.status_code == 200
    assert response.json()[ "name" ] == "Tatyana Updated"
    assert response.json()[ "email" ] == "updated@example.com"