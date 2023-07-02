import psycopg2
from src.read_sql_command_file import ReaderSQLCommandFile
from config.config import *
from src.db_model import DB_Model
from src.read_config import ConfigReader
from src.reader import Reader


def insert_suppliers_data(cur, json_data_suppliers :list[dict]):
    """Insert data from json to the database in TABLE `suppliers"""
    for one_supplier in json_data_suppliers:
        cur.execute(
            """
            INSERT INTO suppliers (company_name, 
                                   contact, 
                                   address, 
                                   phone, 
                                   fax, 
                                   homepage)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING supplier_id
            """,
                                    (one_supplier['company_name'],
                                     one_supplier['contact'],
                                     one_supplier['address'],
                                     one_supplier['phone'],
                                     one_supplier['fax'],
                                     one_supplier['homepage'])
        )
        current_supplier_id = cur.fetchone()[0]
        print('--------------------------------')

        for one_product in one_supplier["products"]:
            cur.execute('SELECT product_id FROM products WHERE product_name = %(pr)s', {'pr':one_product} )
            returned_data = cur.fetchone()
            print("fetchone", returned_data[0])
            # if not returned_data[0]:
            #     continue
            current_product_id = returned_data[0]
            print("pr_id=",current_product_id, one_product)
            print( current_supplier_id, current_product_id)


            cur.execute("UPDATE products SET supplier_id = %s WHERE product_id= %s", (current_supplier_id, current_product_id))
            print("||||||||||||||||||||||")


def add_foreign_keys(cur):
    """ add supplier_id as foreign key for products"""
    cur.execute(
        """ALTER TABLE ONLY products
                            ADD CONSTRAINT fk_products_suppliers 
                            FOREIGN KEY (supplier_id) 
                            REFERENCES suppliers; 
                            """
    )

def main():
    #  we will be connecting to postgres for create DATABASE
    command_reader = ReaderSQLCommandFile()
    create_command = command_reader.get_from_sql(PATH_SQL_CREATOR)
    params = ConfigReader(PATH_DB_INI).get_data("postgresql")       # default base
    # create database
    db = DB_Model('defaulf')
    db.database_creator(create_command, **params)                   # connector will be close

    anything = input("print anything")

    # filling tables from script
    db = DB_Model('my_test_db')
    script_command = command_reader.get_from_sql(PATH_SQL_FILLER)   # read script
    params = ConfigReader(PATH_DB_INI).get_data("my_test_db")       # set new parameters with new DATABASE name
    db.execute_sql_script(script_command, **params)                 # execute filler script, connector still open

    # create table suppliers
    db.execute_sql_script(CREATE_TABLE_SUPPLIERS, **params)
    db.execute_sql_script("ALTER TABLE products ADD COLUMN supplier_id int", **params)

    # read from json
    json_data_suppliers = Reader().get_from_json('../homework-5/suppliers.json')

    try:
        with db.connector.cursor() as cur:

            insert_suppliers_data(cur, json_data_suppliers)
            db.connector.commit()
            print("Данные в suppliers успешно добавлены")

            add_foreign_keys(cur)
            db.connector.commit()
            print(f"FOREIGN KEY успешно добавлены")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db.connector is not None:
            db.close_connector()


if __name__ == '__main__':
    main()
