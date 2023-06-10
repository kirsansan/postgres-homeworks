"""Скрипт для заполнения данными таблиц в БД Postgres."""

from src.reader import Reader
from src.db_model import DB_Model
from config.config import *

def print_all_data_from_csv():
    csfile.print_from_csv(PATH_CUSTOMERS, FIELDS_CUSTOMER_FILE)
    csfile.print_from_csv(PATH_EMPLOYEES, FIELDS_EMPLOYEES_FILE)
    csfile.print_from_csv(PATH_ORDERS, FIELDS_ORDERS_FILE)

def write_to_database():
    bd_model = DB_Model(DB_NAME)
    bd_model.universe_db_saver('customers', csfile.get_from_csv(PATH_CUSTOMERS))
    bd_model.universe_db_saver('employees', csfile.get_from_csv(PATH_EMPLOYEES))
    bd_model.universe_db_saver('orders', csfile.get_from_csv(PATH_ORDERS))


if __name__ == '__main__':
    print("Welcome to Data Base filler")
    csfile = Reader()
    # print_all_data_from_csv()
    write_to_database()
    print("all data have been filled and written")