def user_interaction():
    from src.hh_api import HeadHunterAPI
    from src.vacancy import Vacancy
    from src.JSONSaver import JSONSaver

    hh_api = HeadHunterAPI()
    saver = JSONSaver()

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    hh_vacancies = hh_api.load_vacancies(keyword)

    # Преобразуем в объекты
    vacancy_objects = [Vacancy.from_dict(v) for v in hh_vacancies]

    for vacancy in vacancy_objects:
        saver.add_vacancy(vacancy)

    print("\n[INFO] Вакансии сохранены. Выберите дальнейшее действие:")
    while True:
        print("\n1 - Показать все вакансии")
        print("2 - Показать топ-N по зарплате")
        print("3 - Поиск по ключевому слову")
        print("4 - Удалить вакансию по названию")
        print("0 - Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            for v in saver.get_vacancies():
                print(v)

        elif choice == "2":
            n = int(input("Введите N: "))
            sorted_vacancies = sorted(vacancy_objects, reverse=True)
            for v in sorted_vacancies[:n]:
                print(v)

        elif choice == "3":
            keyword = input("Введите ключевое слово: ").lower()
            results = [
                v for v in vacancy_objects
                if keyword in v.requirement.lower() or keyword in v.responsibility.lower()
            ]
            for v in results:
                print(v)

        elif choice == "4":
            title = input("Введите название (или часть) вакансии для удаления: ")
            saver.delete_vacancy_by_title(title)

        elif choice == "0":
            print("[INFO] Выход.")
            break

        else:
            print("[ERROR] Неверный выбор.")


if __name__ == "__main__":
    user_interaction()
