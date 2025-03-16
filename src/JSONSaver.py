import json
import os
from src.vacancy import Vacancy
from src.file_saver import FileHandler


class JSONSaver(FileHandler):
    """Класс для сохранения вакансий в JSON-файл."""

    def __init__(self, file_name: str = "vacancies.json") -> None:
        self.__file_name = file_name

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в файл."""
        vacancies = self.get_vacancies()

        vacancy_dict = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility,
        }

        if vacancy_dict not in vacancies:
            vacancies.append(vacancy_dict)
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list[dict]:
        """Получает список всех вакансий из файла."""
        if not os.path.exists(self.__file_name):
            return []
        with open(self.__file_name, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из файла по названию (без учёта регистра).
        """
        title_lower = vacancy.title.lower()
        vacancies = self.get_vacancies()

        updated_vacancies = [
            v for v in vacancies if v.get("title", "").lower() != title_lower
        ]

        if len(updated_vacancies) < len(vacancies):
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(updated_vacancies, f, ensure_ascii=False, indent=4)
            print("[INFO] Вакансия успешно удалена.")
        else:
            print("[WARN] Вакансия не найдена.")

