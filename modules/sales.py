from datetime import datetime
from tabulate import tabulate

from database import db_sales
    
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

class ProductList:
    def __init__(self):
        self.product_list = db_sales.get_products()
    def table(self):
        return print(tabulate(self.product_list, headers=['ID', 'Сорт', 'Страна', 'Цена'], tablefmt="grid"))



class Order:
    def __init__(self, user):
        self.user = user
        self.product_list = ProductList()
        self.product_id = None
        self.quantity = None
        self.date = None

    def create_transaction(self):
        self.product_list.table()

        self.product_id = int(input("\n\nУкажите ID нужно товара: "))
        # Проверка количества товара на складе
        # print("Доступно к покупке: {avavailable}")
        self.quantity = int(input('Укажите количество товара: '))
        if quantity <= 0:
            print("Вы указали количество неверно, попробуйте еще раз")
        self.date = datetime.now().date()

    



