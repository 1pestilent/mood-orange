import psycopg2
from database.db_conn import create_connection

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
                CREATE TABLE IF NOT EXISTS permissions(
                id SERIAL PRIMARY KEY NOT NULL,
                permission_name VARCHAR(64))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY NOT NULL,
                sort INTEGER REFERENCES sorts(id),
                country INTEGER REFERENCES countries(id),
                price FLOAT)
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                email VARCHAR(128) PRIMARY KEY NOT NULL UNIQUE,
                last_name VARCHAR(64),
                first_name VARCHAR(64),
                middle_name VARCHAR(64),
                phone_number VARCHAR(32),
                date_of_birth DATE,
                permissions INTEGER REFERENCES permissions(id))
                """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS sales(
                id SERIAL PRIMARY KEY NOT NULL,
                product_id INTEGER REFERENCES products(id),
                user_id VARCHAR(128) REFERENCES users(email),
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