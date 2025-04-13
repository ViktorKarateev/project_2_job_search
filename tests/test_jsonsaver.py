import json
import pytest  # noqa: F401
import os  # noqa: F401
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def test_add_vacancy(tmp_path):
    """Тест добавления вакансии в JSON-файл."""
    test_file = tmp_path / "test_vacancies.json"
    saver = JSONSaver(str(test_file))

    vacancy = Vacancy(
        title="Junior Python Developer",
        url="https://example.com/vacancy",
        salary_from=50000,
        salary_to=70000,
        requirement="Python, Git",
        responsibility="Поддержка внутренних сервисов"
    )

    saver.add_vacancy(vacancy)

    # Читаем файл напрямую
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["title"] == "Junior Python Developer"
    assert data[0]["salary_from"] == 50000
    assert data[0]["responsibility"] == "Поддержка внутренних сервисов"


def test_delete_vacancy(tmp_path):
    """Тест удаления вакансии по полному совпадению объекта."""
    test_file = tmp_path / "test_vacancies.json"
    saver = JSONSaver(str(test_file))

    vacancy = Vacancy(
        title="Middle Developer",
        url="https://example.com/middle",
        salary_from=80000,
        salary_to=120000,
        requirement="Django, REST",
        responsibility="Создание API"
    )

    # Добавим и убедимся, что она добавлена
    saver.add_vacancy(vacancy)
    assert len(saver.get_vacancies()) == 1

    # Удалим и проверим, что список стал пуст
    saver.delete_vacancy(vacancy)
    assert saver.get_vacancies() == []


def test_delete_vacancy_by_title(tmp_path):
    """Тест удаления вакансии по названию (без учёта регистра и по части слова)."""
    test_file = tmp_path / "test_vacancies.json"
    saver = JSONSaver(str(test_file))

    vacancy_1 = Vacancy(
        title="Senior Python Developer",
        url="https://example.com/senior",
        salary_from=150000,
        salary_to=200000,
        requirement="Python, Django",
        responsibility="Ведение проекта"
    )

    vacancy_2 = Vacancy(
        title="Junior Java Developer",
        url="https://example.com/junior",
        salary_from=60000,
        salary_to=90000,
        requirement="Java, Spring",
        responsibility="Помощь в разработке"
    )

    saver.add_vacancy(vacancy_1)
    saver.add_vacancy(vacancy_2)

    # Удалим по слову "python", без учёта регистра
    saver.delete_vacancy_by_title("python")

    vacancies = saver.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Junior Java Developer"


@pytest.fixture
def temp_saver(tmp_path):
    """Фикстура: создает временный файл и Saver."""
    file_path = tmp_path / "test_vacancies.json"
    return JSONSaver(str(file_path))
