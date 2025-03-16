from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass