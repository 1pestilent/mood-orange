import psycopg2
from datetime import datetime

from database.db_conn import create_connection

def add_income(income_type, product_id, quantity):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO income (type_id,product_id ,quantity, date)
        VALUES (%s, %s, %s, %s)
        RETURNING id; """,(income_type, product_id, quantity, datetime.now().date()))

    con.commit()
    cur.close()
    con.close()

    return id

def income_stock(product_id, quantity):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO stock (product_id,quantity)
        VALUES (%s, %s)
        RETURNING id; """,(product_id, quantity))

    con.commit()
    cur.close()
    con.close()

def get_quantity(product_id):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT quantity FROM stock 
        WHERE product_id = %s
        ORDER BY id DESC
        LIMIT 1;""", (product_id,))
    result = cur.fetchone()
    if result is not None:
        quantity = result[0]
    else:
        quantity = 0

    cur.close()
    con.close()  

    return quantity

def history_income():
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT i.id, it.type_name, s.sort_name, c.country_name, i.date, i.quantity FROM income AS i
        JOIN income_types AS it ON it.id = i.type_id
		JOIN products AS p ON i.product_id = p.id
        JOIN sorts AS s ON p.sort = s.id
		JOIN countries AS c ON p.country = c.id
        """)
    result = cur.fetchall()
    result = [[row[0], row[1].title(),row[2].title(),row[3],row[4]] for row in results]

    cur.close()
    con.close()

    return result
