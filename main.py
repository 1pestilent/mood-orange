from database import db_sales
from tabulate import tabulate
import sales

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
