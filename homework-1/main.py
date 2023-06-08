"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from src.utils import Reader
from config.config import *

def db_saver():
    db_connector = psycopg2.connect(
        host='localhost',
        port='5432',
        database='north',
        user='postgres',
        password=DB_PASSWORD
    )

    try:
        with db_connector:
            with db_connector.cursor() as cursor:
                print(cursor)
    finally:
        db_connector.close()


if __name__ == '__main__':
    print("Welcome to")
    db_saver()
    csfile = Reader()
    csfile.print_from_csv(PATH_CUSTOMERS, FIELDS_CUSTOMER_FILE)
    csfile.print_from_csv(PATH_EMPLOYEES, FIELDS_EMPLOYEES_FILE)
    #csfile.print_from_csv(PATH_ORDERS, FIELDS_ORDERS_FILE)



