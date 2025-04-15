with cte1 as (
    select * , ROW_NUMBER() OVER(PARTITION BY product_id order by change_date desc) as rn
    from Products
    where change_date <= "2019-08-16"
)

select p.product_id,
coalesce(c.new_price , 10) as price 
from
(select distinct product_id from Products) p
left join
cte1 c
on p.product_id = c.product_id and c.rn=1;


--- find duplicates and delete
SELECT name, email, department, COUNT(*) AS duplicate_count
FROM Employees
GROUP BY name, email, department
HAVING COUNT(*) > 1;

WITH Ranked AS (
    SELECT id, 
           ROW_NUMBER() OVER (PARTITION BY name, email, department ORDER BY id) AS row_num
    FROM Employees
)
DELETE FROM Employees WHERE id IN (
    SELECT id FROM Ranked WHERE row_num > 1
);


---------
-- find the top 3 customers who have spent the most in the last 6 months."

SELECT customer_id, SUM(order_amount) AS total_spent
FROM Orders
WHERE order_date >= NOW() - INTERVAL 6 MONTH
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 3;


SELECT customer_id, SUM(order_amount) AS total_spent
FROM Orders
WHERE order_date >= CURRENT_DATE - INTERVAL 6 MONTH
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 3;


---------------
-- How would you optimize a slow SQL query that joins multiple tables with billions of records?
-- 1. Indexing
-- 2. proper join
-- 3. partition large tables:
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    order_amount DECIMAL(10,2)
) PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50)
) PARTITION BY LIST (country) (
    PARTITION p_USA VALUES IN ('USA'),
    PARTITION p_CANADA VALUES IN ('Canada'),
    PARTITION p_EUROPE VALUES IN ('UK', 'France', 'Germany')
);

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
) PARTITION BY HASH (user_id) PARTITIONS 4;


4. select and limit
5. materialized views

WITH Filtered AS (
    SELECT *
    FROM Stadium
    WHERE people >= 100
),
Grouped AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Filtered
),
Final AS (
    SELECT *
    FROM Grouped
    WHERE grp IN (
        SELECT grp
        FROM Grouped
        GROUP BY grp
        HAVING COUNT(*) >= 3
    )
)
SELECT id, visit_date, people
FROM Final
ORDER BY visit_date;
