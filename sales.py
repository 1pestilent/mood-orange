from datetime import datetime
from tabulate import tabulate

import sales_funcs

def sale():
    running = True

    while running:
        n = int(input("""--- Выберите действие ---

    1. Посмотреть ассортимент
    2. Сделать заказ
    3. История заказов
    0. Закончить

Выберите действие: """))
        if n == 1:
           pass
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
        n = int(input("""\n--- Выберите действие ---

    1. Посмотреть...
    2. Создать...
    3. История
    4. Склад
    5. Банк
    0. Закончить

Выберите действие: """))
        if n == 1:
            nn = int(input("\nПосмотреть:\n\n1. Товары\n2. Сорта\n3. Страны\n0. Вернуться назад\n\nВыбор: "))
            if nn == 1:
                print('\n')
                products_list = sales_funcs.get_products()
                print(tabulate(products_list, headers=['ID', 'Сорт', 'Страна', 'Цена'], tablefmt="grid"))
            elif nn == 2:
                sorts_list = sales_funcs.sorts()
                print(tabulate(sorts_list, headers=['ID','Сорт'],tablefmt="grid"))
            elif nn == 3:
                countries_list = sales_funcs.countries()
                print(tabulate(countries_list, headers=['ID','Страна'],tablefmt="grid"))
            elif nn == 0:
                pass
            else:
                pass
        elif n == 2:
            nn = int(input("\nСоздать:\n\n1. Товар\n2. Сорт\n3. Страну\n0. Вернуться назад\n\nВыбор: "))
            if nn == 1:
                add_product()
            elif nn == 2:
                add_product_sort()
            elif nn == 3:
                add_product_country()
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

def auth():
    print('\n---Авторизация--_\n ')
    running = True
    while running:
        email = str(input("Укажите Ваш email: "))
        if not sales_funcs.check_user(email):
            print('\n---Вход выполнен успешно---')
            running = False
            return email
        else:
            confirm = int(input('!!! Пользователя с такой почтой не существует !!!\n\n1 - Попробовать ещё раз\n2 - Перейти к регистрации\n\nВвод: '))
            if confirm == 1:
                pass
            elif confirm == 2:
                running = False
                reg()
            

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
    if sales_funcs.check_user(email):
        print(f'\nСоздать пользователя со следующими параметрами:\n\nEmail: {email}\nФИО: {last_name} {first_name} {middle_name}\nНомер телефона: {phone_number}\nДата рождения: {date_of_birth.date()}')
        confirm = int(input('\n1 - cоздать пользователя\n2 - отмена\n\nВвод: '))
        if confirm == 1:
            result = sales_funcs.add_user(email, last_name, first_name,middle_name, phone_number, date_of_birth.date())
            print(f'\nПользователь {email} был успешно создан.')
            return email
        else:
            pass
    else:
        print('\n!!! Пользователь с такой почтой уже существует !!!')

    
def add_product_sort():
    sort_name = str(input("\nВведите название сорта: "))
    if sales_funcs.check_sort(sort_name):
        print(f'\nСорт {sort_name} уже существует!')
    else:
        if sales_funcs.add_sort(sort_name):
            print(f"\nСорт {sort_name} успешно добавлен")
        else:
            print(f"\nДобавить сорт не удалось!")


def add_product_country():
    country_name = str(input("\nВведите название страны: "))
    if sales_funcs.check_country(country_name):
        print(f'\nСорт {country_name} уже существует!')
    else:
        if sales_funcs.add_country(country_name):
            print(f"\nСтрана {country_name} успешно добавлен")
        else:
            print(f"\nДобавить страну не удалось!")

def add_product():
    sorts = sales_funcs.sorts_list()
    countries = sales_funcs.countries_list()

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

    print("""\n--- Добавление товара ---
Выберите сорт апельсина:
""")
    for i in range(len(sorts)):
        print(sorts[i])
        
    sort = int(input("\n Сорт апельсина: "))
    x = True
    while x:
        if 0 < sort <= (len(sorts)+1):
            x = False
        else:
            sort = int(input("\n Вы указали сорт апельсина неверно, попробуйте ещё раз: "))

    print("""\n--- Добавление товара ---
Выберите страну производства:
""")
    countries = [f"{row[0]} - {row[1]}" for row in sales_funcs.countries()]
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
    confirm = int(input(f"""\n--- Вы хотите добавить товар со следущими параметрами: ---

Сорт: {sorts[sort-1]}
Страна: {countries[country-1]}
Цена: {price} руб/шт

--- Подтвердите действие: --- 

1 - продолжить
0 - отменить

Ответ: """))
    if confirm == 1:
        result = sales_funcs.add_product(sort, country, price)
        if result:
            print(f'Товара с данными параметрами был успешно добавлен. ID({result})\n')
        else:
            print('Добавить товар не удалось')
    else:
        print('Добавлена товара отменено!')


def order():
    pass
