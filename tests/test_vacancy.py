import pytest  # noqa: F401
from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест на создание объекта Vacancy."""
    vacancy_data = {
        "name": "Python Developer",
        "alternate_url": "https://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Python, Django", "responsibility": "Backend development"}
    }

    vacancy = Vacancy.from_dict(vacancy_data)

    # Проверяем, что все атрибуты корректно установлены
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://example.com"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.requirement == "Python, Django"
    assert vacancy.responsibility == "Backend development"


def test_vacancy_repr():
    """Тест на корректность строки представления объекта Vacancy."""
    vacancy_data = {
        "name": "Python Developer",
        "alternate_url": "https://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Python, Django", "responsibility": "Backend development"}
    }

    vacancy = Vacancy.from_dict(vacancy_data)

    # Проверяем, что строка представления объекта выглядит как ожидается
    assert repr(vacancy) == "Python Developer - 100000 - 150000"


def test_vacancy_comparison():
    """Тест на сравнение объектов Vacancy по зарплате."""
    vacancy_data_1 = {
        "name": "Python Developer",
        "alternate_url": "https://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Python, Django", "responsibility": "Backend development"}
    }
    vacancy_data_2 = {
        "name": "Java Developer",
        "alternate_url": "https://example.com",
        "salary": {"from": 120000, "to": 160000},
        "snippet": {"requirement": "Java, Spring", "responsibility": "Backend development"}
    }

    vacancy_1 = Vacancy.from_dict(vacancy_data_1)
    vacancy_2 = Vacancy.from_dict(vacancy_data_2)

    # Сравниваем вакансии по зарплате
    assert vacancy_1 < vacancy_2  # vacancy_1 имеет меньшую зарплату, чем vacancy_2
