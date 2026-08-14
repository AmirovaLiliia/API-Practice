# Параметризация на id пользователя

import pytest
import requests


@pytest.mark.parametrize("user_id", [
    999,
    9999,
    123456
])
def test_get_nonexistent_user(user_id):

    response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{user_id}"
)

    assert response.status_code == 404
