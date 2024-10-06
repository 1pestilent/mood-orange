import psycopg2
from datetime import datetime

from db_struct import create_connection

def add_product(con, sort_id, country_id, delivery_date):
    cur = con.cursor()

    cur.execute("""
        INSERT INTO products (sort, country, delivery_date)
        VALUES (%s, %s, %s)
        RETURNING id; """,(sort_id, country_id, delivery_date))
    product_id = cur.fetchone()[0]
    con.commit()
    cur.close()
    con.close()
    return product_id

def add_sale(con, product_id, quantity, customer_email, sale_date):
    cur = con.cursor()

    cur.execute("""
        INSERT INTO sales (product, quantity, customer, date)
        VALUES (%s, %s, %s, %s)
        RETURNING id;""", (product_id, quantity, customer_email, sale_date))
    
    sale_id = cur.fetchone()[0]
    con.commit()
    return sale_id

con = create_connection()
zxc = add_sale(con, 2, 15, 'jordan23@mail.ru', datetime(2024, 10, 24))
print(zxc)