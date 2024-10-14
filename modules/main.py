from database import db_sales
from tabulate import tabulate
from modules import sales

def auth():
    print('\n---Авторизация---\n ')
    running = True
    while running:
        email = str(input("Укажите Ваш email: "))
        if not db_sales.check_user(email):
            print('\n---Вход выполнен успешно---')
            running = False
            return email
        else:
            confirm = int(input('!!! Пользователя с такой почтой не существует !!!\n\n1 - Попробовать ещё раз\n2 - Перейти к регистрации\n\nВвод: '))
            if confirm == 1:
                pass
            elif confirm == 2:
                running = False
                return reg()
            

def reg():
    email = str(input("\n---Создание пользователя---\n\nУкажите Ваш email: "))
    last_name = str(input("Фамилия: "))
    first_name = str(input("Имя: "))
    middle_name = str(input("Отчество: "))
    phone_number = str(input("Номер телефона: "))
    while True:
        try:
            date_of_birth = datetime.strptime(input("Дата рождения в формате (DD.MM.YYYY): "), "%d.%m.%Y")
            break
        except ValueError:
            print("Неправильный формат даты. Пожалуйста, введите дату в формате DD.MM.YYYY\nДата: ")
    if db_sales.check_user(email):
        print(f'\nСоздать пользователя со следующими параметрами:\n\nEmail: {email}\nФИО: {last_name} {first_name} {middle_name}\nНомер телефона: {phone_number}\nДата рождения: {date_of_birth.date()}')
        confirm = int(input('\n1 - cоздать пользователя\n2 - отмена\n\nВвод: '))
        if confirm == 1:
            result = db_sales.add_user(email, last_name, first_name, middle_name, phone_number, date_of_birth.date())
            print(f'\nПользователь {email} был успешно создан.')
            return email
        else:
            pass
    else:
        print('\n!!! Пользователь с такой почтой уже существует !!!')

def sale():
    running = True

    while running:
        n = int(input("""--- Выберите действие ---\n\n1. Посмотреть ассортимент\n2. Сделать заказ\n3. История заказов\n\n0. Закончить\n\nВыберите действие: """))
        if n == 1:
            print('\n')
            products_list = db_sales.get_products()
            print(tabulate(products_list, headers=['ID', 'Сорт', 'Страна', 'Цена'], tablefmt="grid"))
        elif n == 2:
            pass
        elif n == 3:
            pass
        elif n == 0:
            print('\n--- Работа приложения завершена ---\n')
            running = False
        else:
            print(False)


def admin():
    running = True

    while running:
        n = int(input("""\n--- Выберите действие ---\n\n1. Посмотреть...\n2. Создать...\n3. История\n4. Склад\n5. Банк\n\n0. Закончить\n\nВыберите действие: """))
        if n == 1:
            nn = int(input("\nПосмотреть:\n\n1. Товары\n2. Сорта\n3. Страны\n\n0. Вернуться назад\n\nВыбор: "))
            if nn == 1:
                print('\n')
                products_list = db_sales.get_products()
                print(tabulate(products_list, headers=['ID', 'Сорт', 'Страна', 'Цена'], tablefmt="grid"))
            elif nn == 2:
                sorts_list = db_sales.sorts()
                print(tabulate(sorts_list, headers=['ID','Сорт'],tablefmt="grid"))
            elif nn == 3:
                countries_list = db_sales.countries()
                print(tabulate(countries_list, headers=['ID','Страна'],tablefmt="grid"))
            elif nn == 0:
                pass
            else:
                pass
        elif n == 2:
            nn = int(input("\nСоздать:\n\n1. Товар\n2. Сорт\n3. Страну\n\n0. Вернуться назад\n\nВыбор: "))
            if nn == 1:
                sales.add_product()
            elif nn == 2:
                sales.add_product_sort()
            elif nn == 3:
                sales.add_product_country()
            elif nn == 0:
                pass
            else:
                pass
        elif n == 3:
            pass
        elif n == 0:
            print('\n--- Работа приложения завершена ---\n')
            running = False
        else:
            print('')
