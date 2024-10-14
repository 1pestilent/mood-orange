from database import db_stock
from modules.sales import ProductList

def stock_income():
    product_list = ProductList()
    product_list.table()
    product_id = int(input("\nID товара: "))
    quantity = int(input("\nКоличество: "))

    n = int(input(f"Поставка на склад id{product_id} в количестве {quantity}:\n\n1. Продолжить\n0. Отменить\n\nВвод: "))
    if n == 1:
        rid = db_stock.add_income(1, product_id, quantity)
        print(f"\nЗапись была добавлена в таблицу приход/расход: {rid}")
        quantity = db_stock.get_quantity(product_id) + quantity
        db_stock.income_stock(product_id,quantity)
    else:
        pass