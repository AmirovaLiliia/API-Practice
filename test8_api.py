#Параметризация на email

import pytest
import requests


@pytest.mark.parametrize("email", [
    "wrong-email",
    "test@",
    "@email.com",
    ""
])
def test_invalid_email(email):

    data = {
        "name": "Tatyana",
        "username": "Lilia",
        "email": email
    }

    response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
        json=data
)

    print(response.status_code)
    print(response.json())
