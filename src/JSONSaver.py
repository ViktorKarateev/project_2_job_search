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
        vacancies = self.get_vacancies()

        # Преобразуем все поля в нижний регистр для сравнения
        def normalize(vac: dict) -> tuple:
            return (
                vac["title"].lower(),
                vac["url"].lower(),
                str(vac["salary_from"]),
                str(vac["salary_to"]),
                vac["requirement"].lower(),
                vac["responsibility"].lower()
            )

        target = normalize({
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "requirement": vacancy.requirement,
            "responsibility": vacancy.responsibility,
        })

        updated = [v for v in vacancies if normalize(v) != target]

        if len(updated) < len(vacancies):
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump(updated, f, ensure_ascii=False, indent=4)
            print("[INFO] Вакансия удалена.")
        else:
            print("[WARN] Вакансия не найдена.")
