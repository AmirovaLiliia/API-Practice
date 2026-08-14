#Негативные тесты  GET


import requests

def test_get_nonexistent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")


    assert response.status_code == 404

    data = response.json()
    assert data == {}