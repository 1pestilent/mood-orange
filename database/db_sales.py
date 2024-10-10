import psycopg2
from datetime import datetime

from .db_conn import create_connection

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

def add_user(email, last_name,first_name, middle_name, phone_number, date_of_birth):
    con = create_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO users (email, last_name, first_name, middle_name, phone_number, date_of_birth, permissions)
        VALUES (%s, %s, %s, %s, %s, %s, '1')
        RETURNING email; """,(email, last_name, first_name, middle_name, phone_number, date_of_birth))

    user_id = cur.fetchone()[0]

    con.commit()
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

    cur.execute("""SELECT id, sort_name FROM sorts
    ORDER BY id ASC""")
    results = cur.fetchall()
    results = [[row[0], row[1].title()] for row in results]
    cur.close()
    con.close()

    return results

def sorts_list():
        sort_list = [f"{row[0]} - {row[1]}" for row in sorts()]
        if len(sort_list) == 0:
            return print('\n!!! В базе данных нет ни одного сорта !!! \n')
        else:
            return sort_list

def countries():
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT id, country_name FROM countries
    ORDER BY id ASC""")
    results = cur.fetchall()
    results = [[row[0], row[1].title()] for row in results]
    cur.close()
    con.close()

    return results

def countries_list():
    countries_list = [f"{row[0]} - {row[1]}" for row in countries()]
    if len(countries_list) == 0:
        return print('\n!!! В базе данных нет ни одной страны !!!\n')   
    else:
        return countries_list

def add_sort(sort_name):

    con = create_connection()
    cur = con.cursor()

    sort = sort_name.lower().strip()

    cur.execute("""INSERT INTO sorts (sort_name)
        VALUES (%s)
        RETURNING id;""", (sort,))
    
    sort_id = cur.fetchone()[0]

    con.commit()
    cur.close()
    con.close()

    return sort_id

def check_sort(sort_name):
    con = create_connection()
    cur = con.cursor()

    sort = sort_name.lower().strip()
    cur.execute("""
        SELECT id FROM sorts
        WHERE sort_name = (%s)""", (sort,))
    try:
        sort_id = cur.fetchone()[0]
        return sort_id
    except:
        return False

    cur.close()
    con.close()

    return sort_id    

def add_country(country_name):
    
    con = create_connection()
    cur = con.cursor()

    country = country_name.lower().strip()

    cur.execute("""
        INSERT INTO countries (country_name)
        VALUES (%s)
        RETURNING id;""", (country,))
    
    country_id = cur.fetchone()[0]

    con.commit()
    cur.close()
    con.close()

    return country_id

def check_country(country_name):
    con = create_connection()
    cur = con.cursor()

    country = country_name.lower().strip()
    cur.execute("""
        SELECT id FROM countries
        WHERE country_name = (%s)""", (country,))
    try:
        country_id = cur.fetchone()[0]
        return country_id
    except:
        return False

    cur.close()
    con.close()

    return country_id    

def get_products():
    con = create_connection()
    cur = con.cursor()

    cur.execute("""SELECT p.id, s.sort_name, c. country_name, p.price FROM products AS p
        JOIN sorts AS s ON p.sort = s.id
        JOIN countries AS c ON p.country = c.id""")
    products = cur.fetchall()
    products_list = []
    for row in products:
        if row[2] == 'сша':
            products_list.append((row[0], row[1].title(), row[2].upper(), row[3]))
        else:
            products_list.append((row[0], row[1].title(), row[2].title(), row[3]))

    cur.close()
    con.close()
    return products_list