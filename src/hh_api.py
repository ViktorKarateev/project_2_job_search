import requests
from typing import List, Dict
from src.base_api import APIHandler


class HeadHunterAPI(APIHandler):
    """
    Класс для работы с API hh.ru.
    Реализует метод получения вакансий по ключевому слову.
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-Job-Search-App"}
        self.__params = {
            "text": "",
            "page": 0,
            "per_page": 20
        }

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Получает вакансии с hh.ru по ключевому слову.
        :param keyword: Строка поиска
        :return: Список вакансий (словари)
        """
        self.__params["text"] = keyword
        self.__params["page"] = 0

        all_vacancies = []

        while self.__params["page"] < 5:  # ограничим 5 страницами
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )

            if response.status_code != 200:
                print(f"Ошибка при запросе: {response.status_code}")
                break

            data = response.json()
            vacancies = data.get("items", [])
            all_vacancies.extend(vacancies)

            self.__params["page"] += 1

        return all_vacancies
