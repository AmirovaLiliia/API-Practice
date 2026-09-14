import pytest
import requests
from config import BASE_URL


@pytest.mark.positive
def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

    expected_user = {
    "id": 1,
    "name": "Leanne Graham"
}

    assert data["id"] == expected_user["id"]
    assert data["name"] == expected_user["name"]
    assert "@" in data["email"]
    #assert data["email"] == "leanne@gmail.com"
    assert "." in data["email"]


    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)




@pytest.mark.negative
@pytest.mark.parametrize("user_id", [
    999,
    9999,
    123456
])
def test_get_nonexistent_user(user_id):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}"
    )

    assert response.status_code == 404
    assert response.json() == {}



