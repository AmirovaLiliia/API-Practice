import pytest
import requests
from config import BASE_URL


def test_create_user():
    data = {
        "name": "Tatyana",
        "username": "Lilia",
        "email": "tatyana@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=data
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Tatyana"
    assert response.json()["email"] == "tatyana@example.com"

