from src.hh_api import HeadHunterAPI

api = HeadHunterAPI()
vacancies = api.get_vacancies("Python")

print(f"Найдено вакансий: {len(vacancies)}")
print(vacancies[0])  # Вывести первую вакансию
