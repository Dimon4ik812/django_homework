# Интернет магшазин
## Описание:
Интернет магазин
## Установка:
1. Клонируйте репозиторий:
```
https://github.com/Dimon4ik812/django_homework/tree/feature/homework_22
```
2. Установите зависимости:
```
pip install poetry
poetry install
poetry add requests
pip install pytest
pip install  pytest-cov
poetry add python-dotenv 
poetry add --group lint mypy
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint flake8 
poetry add requests-mock

```
## Тестирование
С помощью линтеров mypy, black, flake8, isort можете проверить код на соответствие PEP8
Пример команды:
```
flake8 module_name
flake8 . (все модули)
```

## Test Coverage
При необходимости можете проверить с помощью команд:
```
poetry add --group dev pytest
pytest --cov 
```


