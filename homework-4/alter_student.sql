CREATE DATABASE students
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
( student_id serial PRIMARY KEY,
  first_name varchar,
  last_name varchar,
  birthday date,
  phone varchar
);


-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date, phone ) VALUES ('Mark', 'Avrelii', '121-04-26', 'nothing');
INSERT INTO student (first_name, last_name, birth_date, phone ) VALUES ('Julius', 'Caesar', '0100-07-12 BC', 'call me by the Bell');
INSERT INTO student (first_name, last_name, birth_date, phone ) VALUES ('Octavianus', 'Augustus', '0014-08-14', 'call me by the Bell two times');


--INSERT INTO student (first_name, last_name, birth_date, phone ) VALUES ('Mark', 'Avrelii', '121-04-26', 'nothing');
--INSERT INTO student (first_name, last_name, birth_date, phone ) VALUES ('Julius', 'Caesar', '0100-07-12 BC', 'call me by the Bell'),
--																	   ('Octavianus', 'Augustus', '0014-08-14', 'call me by the Bell two times');


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;