--SELECT pg_terminate_backend(pg_stat_activity.pid)
--FROM pg_stat_activity
--WHERE pg_stat_activity.datname = 'my_test_db' -- your BD name
--  AND pid <> pg_backend_pid();
--
--DROP DATABASE my_test_db;

CREATE DATABASE my_test_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
