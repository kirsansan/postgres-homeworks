-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
ALTER TABLE products ADD CONSTRAINT check_product_price CHECK(products.unit_price>0);

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1
ALTER TABLE products ADD CONSTRAINT check_product_discontinued CHECK(products.discontinued IN (0,1) );


-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
SELECT * INTO discontinued_products FROM products
WHERE discontinued=1;

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

-- бэкапим из order_details все строки заказов, снятых с продажи
SELECT * INTO backup_order_details FROM order_details
WHERE product_id IN (SELECT product_id FROM products WHERE discontinued=1)

-- удаляем их из order_details
DELETE FROM order_details
WHERE product_id IN (SELECT product_id FROM products WHERE discontinued=1)

-- удаляем снятое с продаж из products в соответствии с заданием
DELETE FROM products WHERE discontinued=1;