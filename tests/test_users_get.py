import pytest
import requests
from config import BASE_URL

def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]




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



