import requests
from abc import ABC
from typing import List, Dict
from src.base_api import APIHandler


class HeadHunterAPI(APIHandler, ABC):
    """
    Класс для работы с API hh.ru.
    Реализует метод получения вакансий по ключевому слову.
    """

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-Job-Search-App"}
        self.params: dict[str, str | int] = {
            "text": "",
            "page": 0,
            "per_page": 20
        }
        self.vacancies: List[Dict] = []

    def connect(self) -> None:
        """
        Заглушка метода подключения к API hh.ru.
        Пока подключение не требуется, но метод реализован для соответствия абстракции.
        """
        print("[INFO] Подключение к API hh.ru успешно (заглушка)")

    def load_vacancies(self, keyword: str) -> List[Dict]:
        """Загрузка вакансий с hh.ru по ключевому слову"""
        self.params["text"] = keyword
        self.params["page"] = 0
        self.vacancies = []

        while int(self.params["page"]) < 1:
            response = requests.get(
                self.url,
                headers=self.headers,
                params=self.params
            )

            if response.status_code != 200:
                print(f"[ERROR] Ошибка запроса: {response.status_code}")
                break

            data = response.json()
            self.vacancies.extend(data.get("items", []))
            self.params["page"] = int(self.params ["page"]) + 1

        print(f"[INFO] Найдено вакансий: {len(self.vacancies)}")
        return self.vacancies

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Реализация абстрактного метода получения вакансий"""
        return self.load_vacancies(keyword)
