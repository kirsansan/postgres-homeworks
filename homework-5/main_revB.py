import psycopg2
from src.read_sql_command_file import ReaderSQLCommandFile
from config.config import *
from src.db_model import DB_Model
from src.read_config import ConfigReader


def main():
    # for create DATABASE will be connecting to postgres
    command_reader = ReaderSQLCommandFile()
    create_command = command_reader.get_from_sql(PATH_SQL_CREATOR)
    params = ConfigReader(PATH_DB_INI).get_data("postgresql")  # default base
    db = DB_Model('my_test_db')

    # create
    db.database_creator(create_command, **params)

    # filling from script
    script_command = command_reader.get_from_sql(PATH_SQL_FILLER)  # read script
    params = ConfigReader(PATH_DB_INI).get_data("my_test_db")  # set new parameters with new DATABASE name
    db.execute_sql_script(script_command, **params)  # execute script

    script_command = """
                        CREATE TABLE suppliers (
                        supplier_id smallint NOT NULL,
                        company_name character varying(40) NOT NULL,
                        contact character varying(30),
                        address character varying(60),
                        phone character varying(24),
                        fax character varying(24),
                        homepage text
                        );
                        """
    db.execute_sql_script(script_command, **params)


if __name__ == '__main__':
    main()
