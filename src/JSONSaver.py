import json
import os
from src.vacancy import Vacancy
from src.file_saver import FileHandler


class JSONSaver(FileHandler):
    """Класс для сохранения вакансий в JSON-файл."""

    def __init__(self, file_name: str = "vacancies.json") -> None:
        self.__file_name = file_name

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()

        # Конвертируем объект в словарь
        vacancy_dict = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility,
        }

        # Проверка на дубль
        if vacancy_dict not in vacancies:
            vacancies.append(vacancy_dict)
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list[dict]:
        if not os.path.exists(self.__file_name):
            return []
        with open(self.__file_name, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из файла по совпадению всех полей."""
        vacancies = self.get_vacancies()

        # Создаем словарь из переданного объекта
        vacancy_dict = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility
        }

        if vacancy_dict in vacancies:
            vacancies.remove(vacancy_dict)
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(vacancies, file, indent=2, ensure_ascii=False)
            print(f"[INFO] Вакансия удалена: {vacancy.title}")
        else:
            print(f"[WARNING] Вакансия не найдена: {vacancy.title}")

