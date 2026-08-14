# API Automation Tests

Автоматизированное тестирование REST API с использованием Python, pytest и requests.

## 🛠 Технологии

- Python
- Pytest
- Requests
- REST API
- JSON

## 📁 Структура проекта

```text
API/
├── tests/
│   ├── └── test_py
│   ├── test_users_get.py
│   └── test_users_post.py
│
├── config.py
├── pytest.ini
└── README.md
🚀 Установка
Клонировать проект и установить зависимости:
pip install pytest requests
▶️ Запуск тестов
Запустить все тесты:
pytest
Запустить тесты с подробным выводом:
pytest -v
Запустить только GET-тесты:
pytest tests/test_users_get.py
Запустить только POST-тесты:
pytest tests/test_users_post.py
Запустить негативные тесты:
pytest -m negative
Запустить позитивные тесты:
pytest -m positive
🧪 Покрытие
На данный момент реализованы:
GET — получение пользователя
GET — проверка несуществующего пользователя
POST — создание пользователя
Негативные сценарии
Параметризация тестов
Pytest fixtures
Pytest markers
🔗 API
Для обучения используется JSONPlaceholder:
https://jsonplaceholder.typicode.com (https://jsonplaceholder.typicode.com/)/
📊 Результат
Все реализованные автотесты должны завершаться успешно:
passed