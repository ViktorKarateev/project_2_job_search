import json
import os
from src.vacancy import Vacancy
from src.file_saver import FileHandler


class JSONSaver(FileHandler):
    """Класс для сохранения вакансий в JSON-файл."""

    def __init__(self, file_name: str = "data/vacancies.json") -> None:
        # Создаём директорию, если её нет
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
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
        """Удаляет вакансию по полному совпадению объекта."""
        vacancies = self.get_vacancies()

        vacancy_dict = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility,
        }

        if vacancy_dict in vacancies:
            vacancies.remove(vacancy_dict)
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
            print("[INFO] Вакансия удалена по объекту.")
        else:
            print("[WARN] Вакансия не найдена при удалении по объекту.")

    def delete_vacancy_by_title(self, title: str) -> None:
        """
        Удаляет вакансию по названию (без учёта регистра и по части слова).
        Используется в main.py для взаимодействия с пользователем.
        """
        vacancies = self.get_vacancies()
        title_lower = title.lower()

        updated_vacancies = [
            v for v in vacancies if title_lower not in v.get("title", "").lower()
        ]

        if len(updated_vacancies) < len(vacancies):
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(updated_vacancies, f, ensure_ascii=False, indent=4)
            print("[INFO] Вакансия успешно удалена.")
        else:
            print("[WARN] Вакансия не найдена.")
