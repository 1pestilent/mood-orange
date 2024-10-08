import sales_funcs
from datetime import datetime

def sales():
    running = True

    while running:
        n = int(input("""--- Выберите действие ---

    1. Добавить товар
    2. Добавить покупателя
    3. Добавить продажу
    0. Закончить

Выберите действие: """))
        if n == 1:
           add_product()
        elif n == 0:
            print('\n--- Работа приложения завершена ---\n')
            running = False
        else:
            print(False)


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
    pass
def add_product_country():
    pass

def add_product():
    sorts = [f"{row[0]} - {row[1]}" for row in sales_funcs.sorts()]
    if len(sorts) == 0:
        print('\n!!! В базе данных нет ни одного сорта !!! \n')
        return
    else:
        pass

    countries = [f"{row[0]} - {row[1]}" for row in sales_funcs.countries()]
    if len(countries) == 0:
        print('\n!!! В базе данных нет ни одной страны !!!\n')
        return
    else:
        pass

    print("""\n--- Добавление товара ---
Выберите сорт апельсина:
""")
    for i in range(len(sorts)):
        print(sorts[i])
        
    sort = int(input("\n Сорт апельсина: "))
    x = True
    while x:
        if 0 < sort < (len(sorts)+1):
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