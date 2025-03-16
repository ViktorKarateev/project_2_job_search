from typing import Optional


class Vacancy:
    """
    Класс для представления вакансии как объекта.
    """

    __slots__ = ("title", "url", "salary_from", "salary_to", "requirement", "responsibility")

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        requirement: Optional[str],
        responsibility: Optional[str]
    ):
        self.title = title
        self.url = url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.requirement = requirement or "Не указано"
        self.responsibility = responsibility or "Не указано"

    @staticmethod
    def _validate_salary(value: Optional[int]) -> int:
        """
        Валидирует значение зарплаты.
        Если значение None — возвращает 0.
        """
        return value if value is not None else 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_from < other.salary_from

    def __eq__(self, other: "Vacancy") -> bool:
        return self.salary_from == other.salary_from

    def __str__(self) -> str:
        return (
            f" {self.title}\n"
            f" {self.url}\n"
            f" Зарплата: от {self.salary_from} до {self.salary_to} руб.\n"
            f" Требования: {self.requirement}\n"
            f" Обязанности: {self.responsibility}\n"
        )
