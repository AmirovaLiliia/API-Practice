import pytest
import requests
from config import  BASE_URL


@pytest.fixture
def user_data():
    return {
        "name": "Tom",
        "username": "Tom_user",
        "email": "tom@example.com"
    }


def test_create_user(user_data):


    response = requests.post(
        f"{BASE_URL}/users",
        json=user_data
    )
    response_data = response.json()

    expected_data = {"name": "Tom",
            "username": "Tom_user",
            "email": "tom@example.com"
                     }

    assert response.status_code == 201
    assert response_data["name"] == user_data["name"]
    assert response_data["username"] == user_data["username"]
    assert response_data["email"] == user_data["email"]
    assert "id" in response_data
    assert isinstance(response_data["id"], int)

    print(user_data)



@pytest.mark.negative
def test_create_user_without_email():
    data = {"name": "Tom",
            "username": "Tom_user"
            }
    response = requests.post(
        f"{BASE_URL}/users",
        json = data
    )

    assert  response.status_code == 400
    print(response.status_code)
    print(response.json())



