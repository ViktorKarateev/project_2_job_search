from abc import ABC, abstractmethod
from typing import List, Dict


class APIHandler(ABC):
    """
    Абстрактный класс для API-сервисов по вакансиям.
    Все наследники должны реализовать метод get_vacancies.
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """
        Метод для получения списка вакансий по ключевому слову.
        Должен быть реализован в наследниках.
        :param keyword: Ключевое слово для поиска вакансий
        :return: Список словарей с вакансиями
        """
        pass

    @abstractmethod
    def connect(self) -> None:
        """Метод подключения к API."""
        pass
