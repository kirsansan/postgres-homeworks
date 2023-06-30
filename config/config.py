# for dotenv install  python-dotenv

import os
from dotenv import load_dotenv


load_dotenv()

DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')

DB_NAME = 'north'


PATH_CUSTOMERS = './north_data/customers_data.csv'
PATH_EMPLOYEES = './north_data/employees_data.csv'
PATH_ORDERS = './north_data/orders_data.csv'


FIELDS_CUSTOMER_FILE = ("customer_id","company_name","contact_name")
FIELDS_EMPLOYEES_FILE = ("employee_id","first_name","last_name","title","birth_date","notes")
FIELDS_ORDERS_FILE = ("order_id","customer_id","employee_id","order_date","ship_city")


PATH_SQL_CREATOR = '../homework-5/create_db.sql'
PATH_SQL_FILLER = '../homework-5/fill_db.sql'
PATH_DB_INI = '../config/database.ini'