import psycopg2
from db_conn import create_connection

def create_tables(con):
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS sorts(
                id SERIAL PRIMARY KEY NOT NULL,
                sort_name VARCHAR(64))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS countries(
                id SERIAL PRIMARY KEY NOT NULL,
                country_name VARCHAR(64))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS income_types(
                id SERIAL PRIMARY KEY NOT NULL,
                type_name VARCHAR(64))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS transaction_types(
                id SERIAL PRIMARY KEY NOT NULL,
                type_name VARCHAR(64))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY NOT NULL,
                sort INTEGER REFERENCES sorts(id),
                country INTEGER REFERENCES countries(id),
                price FLOAT)
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS customers(
                email VARCHAR(128) PRIMARY KEY NOT NULL,
                last_name VARCHAR(64),
                first_name VARCHAR(64),
                middle_name VARCHAR(64),
                phone_number VARCHAR(32),
                date_of_birth DATE)
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS sales(
                id SERIAL PRIMARY KEY NOT NULL,
                product_id INTEGER REFERENCES products(id),
                customer VARCHAR(128) REFERENCES customers(email),
                quantity INTEGER,
                total_amount FLOAT,
                date TIMESTAMP)
                """)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS stock(
                id SERIAL PRIMARY KEY NOT NULL,
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER)
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS income(
                id SERIAL PRIMARY KEY NOT NULL,
                type_id INTEGER REFERENCES income_types(id),
                product_id INTEGER REFERENCES products(id),
                quantity INTEGER,
                date TIMESTAMP)
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS bank(
                id SERIAL PRIMARY KEY NOT NULL,
                balance FLOAT)
                """)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS transactions(
                id SERIAL PRIMARY KEY NOT NULL,
                type_id INTEGER REFERENCES transaction_types(id),
                amount FLOAT,
                date TIMESTAMP)
                """)
    

    

    con.commit()
    cur.close()
    con.close()

conn = create_connection()
create_tables(conn)