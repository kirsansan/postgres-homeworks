import psycopg2
from config.config import *


class DB_Model:

    def __init__(self, db_name):
        self.db_name = db_name

    def print_cursor(self):
        """ test for create cursor for database and print it
        this method needs me for a tests"""
        db_connector = psycopg2.connect(
            host='localhost',
            port='5432',
            database=self.db_name,
            user='postgres',
            password=DB_PASSWORD
        )
        try:
            with db_connector:
                with db_connector.cursor() as cursor:
                    print(cursor)
        finally:
            db_connector.close()

    def universe_db_saver(self, table_name, data_as_tuples):
        """ fill the database with the given data_as_tuples
        order of fills must be the same in table and tuples"""
        if not data_as_tuples:
            return None

        # I believe all data in data_as_tuples have the same structure.
        # so I can see it in the first one
        values_string = self.value_creator(len(data_as_tuples[0]))

        db_connector = psycopg2.connect(
            host='localhost',
            port='5432',
            database=self.db_name,
            user='postgres',
            password=DB_PASSWORD
        )
        try:
            with db_connector:
                with db_connector.cursor() as cursor:
                    for row in data_as_tuples:
                        cursor.execute(f"INSERT INTO {table_name} {values_string}", row)
        finally:
            db_connector.close()

    def execute_sql_script(self, command, **params):
        """ create the database
        params is dict with parameters for postgreSQL
        """

        db_connector = psycopg2.connect(
            host=params['host'],
            port=params['port'],
            database=params['database'],
            user=params['user'],
            password=DB_PASSWORD
        )
        try:
            with db_connector:
                with db_connector.cursor() as cursor:
                    cursor.execute(command)
        finally:
            db_connector.close()

    def database_creator(self, command, **params):
        """ create the database
        params is dict with parameters for postgreSQL
        """

        db_connector = psycopg2.connect(
            host=params['host'],
            port=params['port'],
            database=params['database'],
            user=params['user'],
            password=DB_PASSWORD
        )
        db_connector.autocommit = True
        cursor = db_connector.cursor()
        cursor.execute(command)
        cursor.close()
        db_connector.close()


    @staticmethod
    def value_creator(number: int):
        """
        create string for multi-filling values in INSERT command
        :param: number of values
        :return: string like as VALUES(%s, %s, %s,... %s)
        """
        tmp_string = 'VALUES('
        for i in range(0, number):
            if i == number - 1:
                tmp_string += '%s'
            else:
                tmp_string += '%s, '
        tmp_string += ')'
        return tmp_string
