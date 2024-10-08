import psycopg2
from datetime import datetime

from db_conn import create_connection

def add_product(sort, country, price):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO products (sort, country, price)
        VALUES (%s, %s, %s)
        RETURNING id; """,(sort, country, price))

    product_id = cur.fetchone()[0]

    con.commit()
    cur.close()
    con.close()

    return product_id

def get_permisson(email):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT permissions FROM users WHERE email = %s""",(email,))
    permission = cur.fetchone()[0]

    cur.close()
    con.close()

    return permission

def check_user(email):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT * FROM users WHERE email = %s""",(email,))
    exist = cur.fetchall()

    if not exist:
        return True
    else:
        return False

    cur.close()
    con.close()

def add_user(email, last_name,first_name,middle_name,phone_number,date_of_birth,permission = 1):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO users (email, last_name, first_name, middle_name, phone_number, date_of_birth, permissions)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING email; """,(email, last_name, first_name, middle_name, phone_number, date_of_birth,permission))

    user_id = cur.fetchone()[0]

    cur.close()
    con.close()

    return user_id

def add_sale(product_id, user_id, quantity, date):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO sales (product_id, user_id, quantity, date)
        VALUES (%s, %s, %s, %s)
        RETURNING id;""", (product_id, user_id, quantity, date))
    
    sale_id = cur.fetchone()[0]

    con.commit()
    cur.close()
    con.close()

    return sale_id

def sorts():
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT id, sort_name FROM sorts""")
    results = cur.fetchall()

    cur.close()
    con.close()

    return results

def countries():
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT id, country_name FROM countries""")
    results = cur.fetchall()

    cur.close()
    con.close()

    return results

def add_sort():
    pass

def add_country():
    pass
