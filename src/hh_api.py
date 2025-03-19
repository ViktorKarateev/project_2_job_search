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
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-Job-Search-App"}
        self.__params: dict[str, str | int] = {
            "text": "",
            "page": 0,
            "per_page": 20
        }
        self.__vacancies: List[Dict] = []

    def connect(self) -> None:
        """Проверка подключения к API hh.ru"""
        try:
            response = requests.get(self.__url, headers=self.__headers, params={"text": "python"})
            response.raise_for_status()
            print("[INFO] Подключение к API hh.ru успешно.")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Ошибка подключения к API: {e}")

    def __load_vacancies(self, keyword: str) -> List[Dict]:
        """Загрузка вакансий с hh.ru по ключевому слову"""
        self.__params["text"] = keyword
        self.__params["page"] = 0
        self.__vacancies = []

        while int(self.__params["page"]) < 1:

            try:
                response = requests.get(
                    self.__url,
                    headers=self.__headers,
                    params=self.__params
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Ошибка при запросе вакансий: {e}")
                break

            data = response.json()
            self.__vacancies.extend(data.get("items", []))
            self.__params["page"] = int(self.__params["page"]) + 1

        print(f"[INFO] Найдено вакансий: {len(self.__vacancies)}")
        return self.__vacancies

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Реализация абстрактного метода получения вакансий"""
        return self.__load_vacancies(keyword)
