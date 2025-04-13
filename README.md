# Курсовой проект: Поиск вакансий (project_2_job_search)

## Описание
Консольное Python-приложение для поиска вакансий с сайта HeadHunter (hh.ru), фильтрации и сохранения данных.  
Проект реализован с применением принципов ООП, типизации, абстракций и тестирования.

---

## Структура проекта

```
project_2_job_search/
├── data/                    # Директория для хранения JSON-файлов
├── htmlcov/                 # Отчёт по покрытию тестами
├── src/                     # Исходный код
│   ├── base_api.py          # Абстрактный класс APIHandler
│   ├── hh_api.py            # Класс HeadHunterAPI для работы с API hh.ru
│   ├── JSONSaver.py         # Класс JSONSaver для сохранения вакансий
│   ├── vacancy.py           # Класс Vacancy — объект вакансии
│   └── __init__.py
├── tests/                   # Модульные тесты
│   ├── test_vacancy.py
│   ├── test_jsonsaver.py
│   └── __init__.py
├── main.py                  # Консольный интерфейс пользователя
├── README.md                # Документация проекта
├── .gitignore               # Исключения для Git
├── .flake8                  # Настройки стиля кода
├── poetry.lock              # Зависимости проекта
├── pyproject.toml           # Конфигурация Poetry
├── .coverage                # Покрытие тестами
```

---

## Основной функционал

- Загрузка вакансий с сайта hh.ru по ключевому слову
- Преобразование данных в объекты `Vacancy`
- Сохранение и удаление вакансий из JSON-файла (`JSONSaver`)
- Удаление:
  - по точному совпадению (`delete_vacancy`)
  - по названию, без учёта регистра (`delete_vacancy_by_title`)
- Сортировка вакансий по `salary_from` (`__lt__`, `__eq__`)
- Поиск по ключевым словам в требованиях и обязанностях
- Консольный интерфейс с выбором действия

---

## Тестирование

- Используется `pytest` и `coverage`
- Покрытие кода: **94%**
- Протестированы:
  - Создание объектов `Vacancy`
  - Сравнение, сортировка, строковое представление
  - Добавление, удаление, фильтрация вакансий (`JSONSaver`)
- Генерация отчёта покрытия:
```bash
poetry run coverage run -m pytest
poetry run coverage report
poetry run coverage html   # htmlcov/index.html
```

---

## 🔍 Проверка кода

- `flake8` — стиль кода (PEP8)
- `mypy` — статическая типизация

Запуск:
```bash
poetry run flake8 src/ tests/ main.py
poetry run mypy src/ tests/ main.py
```

---

## Установка и запуск

Клонировать репозиторий:
```bash
git clone <ссылка>
cd project_2_job_search
```

Установить зависимости:
```bash
poetry install
```

Запустить проект:
```bash
poetry run python main.py
```

Запустить тесты:
```bash
poetry run pytest
```

---

##  Автор

Каратеев Виктор
