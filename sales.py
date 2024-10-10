from datetime import datetime
from database import db_sales

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

    
def add_product_sort():
    sort_name = str(input("\nВведите название сорта: "))
    if db_sales.check_sort(sort_name):
        print(f'\nСорт {sort_name} уже существует!')
    else:
        if db_sales.add_sort(sort_name):
            print(f"\nСорт {sort_name} успешно добавлен")
        else:
            print(f"\nДобавить сорт не удалось!")


def add_product_country():
    country_name = str(input("\nВведите название страны: "))
    if db_sales.check_country(country_name):
        print(f'\nСорт {country_name} уже существует!')
    else:
        if db_sales.add_country(country_name):
            print(f"\nСтрана {country_name} успешно добавлен")
        else:
            print(f"\nДобавить страну не удалось!")

def add_product():
    sorts = db_sales.sorts_list()
    countries = db_sales.countries_list()

    if not sorts:
        n = int(input("Cоздать сорт:\n\n1. Да\n2. Нет\n\nВыбор: "))
        if n == 1:
            add_product_sort()
            return
        else:
            return
    if not countries:
        n = int(input("Cоздать страну:\n\n1. Да\n2. Нет\n\nВыбор: "))
        if n == 1:
            add_product_country()
            return
        else:
            return

    print("\n--- Добавление товара ---\nВыберите сорт апельсина:")
    for i in range(len(sorts)):
        print(sorts[i])
        
    sort = int(input("\n Сорт апельсина: "))
    x = True
    while x:
        if 0 < sort <= (len(sorts)+1):
            x = False
        else:
            sort = int(input("\n Вы указали сорт апельсина неверно, попробуйте ещё раз: "))

    print("\n--- Добавление товара ---\nВыберите страну производства:\n\n")
    countries = [f"{row[0]} - {row[1]}" for row in db_sales.countries()]
    for i in range(len(countries)):
        print(countries[i])
        
    country = int(input("\n Страна апельсина: "))
    x = True
    while x:
        if 0 < country < (len(countries)+1):
            x = False
        else:
            sort = int(input("Вы указали страну неверно, попробуйте ещё раз: "))   
    price = float(input("\n Укажите цену за штуку: "))
    confirm = int(input(f"\n--- Вы хотите добавить товар со следущими параметрами: ---\n\nСорт: {sorts[sort-1]}\nСтрана: {countries[country-1]}\nЦена: {price} руб/шт\n\n--- Подтвердите действие: ---\n\n1 - продолжить\n0 - отменить\n\nОтвет: "))
    if confirm == 1:
        result = db_sales.add_product(sort, country, price)
        if result:
            print(f'Товара с данными параметрами был успешно добавлен. ID({result})\n')
        else:
            print('Добавить товар не удалось')
    else:
        print('Добавлена товара отменено!')


def order():
    pass
