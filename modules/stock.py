from database import db_stock, db_sales
from modules.sales import ProductList

def stock_income():
    product_list = ProductList()
    product_list.table()
    product_id = int(input("\nID товара: "))
    quantity = int(input("\nКоличество: "))

    n = int(input(f"Поставка на склад id{product_id} в количестве {quantity}:\n\n1. Продолжить\n0. Отменить\n\nВвод: "))
    if n == 1:
        db_stock.add_income(1, product_id, quantity)
        print(f"\nЗапись была добавлена в таблицу приход/расход")
        quantity = db_stock.get_quantity(product_id) + quantity
        db_stock.income_stock(product_id,quantity)
    else:
        pass

def stock_expense():
    product_list = ProductList()
    product_list.table()
    product_id = int(input("\nID товара: "))
    while not db_sales.check_product(product_id):
        product_id = int(input("Вы указали ID не верно, попробуйте ещё раз: "))
    else:
        pass
    quantity = int(input("\nКоличество: "))
    stock = db_stock.get_quantity(product_id)
    if stock == 0:
        return
    else:
        while not 0 <= quantity < stock:
            quantity = int(input("Вы указали количество не верно, попробуйте ещё раз: "))
        else:
            n = int(input(f"\nСписание товара со склада id{product_id} в количестве {quantity}:\n\n1. Продолжить\n0. Отменить\n\nВвод: "))
            if n == 1:
                db_stock.add_income(2, product_id, quantity)
                print(f"\nЗапись была добавлена в таблицу приход/расход")
                quantity = db_stock.get_quantity(product_id) - quantity
                db_stock.income_stock(product_id,quantity)
            else:
                return 