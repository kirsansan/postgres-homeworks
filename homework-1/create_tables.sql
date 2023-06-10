-- SQL-команды для создания таблиц

CREATE TABLE customers
( customer_id char (5) PRIMARY KEY,
  company_name char (100),
  contact_name char (50)
);

CREATE TABLE employees
( employee_id int PRIMARY KEY,
  first_name char (20),
  last_name char (20),
  title char (100),
  birth_date char (10),
  notes text
);

CREATE TABLE orders
(	order_id int PRIMARY KEY,
 	customer_id char (6) UNIQUE REFERENCES customers (customer_id),
 	employee_id int UNIQUE REFERENCES employees (employee_id),
 	order_date char (10),
 	shio_city char (30)
);
