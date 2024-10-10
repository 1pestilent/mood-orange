import psycopg2
from datetime import datetime

from database.db_conn import create_connection

def add_income(income_type, product_id, quantity, date):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO income (income_type,product_id ,quantity, date)
        VALUES (%s, %s, %s, %s)
        RETURNING id; """,(income_type, product_id, quantity, date))

    con.commit()
    cur.close()
    con.close()

    return id

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
