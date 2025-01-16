
create database db1;
create database if not exists db1;

drop database if exists db1;
drop database db1;

use database db1;

show databases;
show tables;

CREATE TABLE person (
    person_id INT PRIMARY KEY,                -- Integer type for unique identifier
    first_name VARCHAR(50) NOT NULL,                   -- Variable-length string for first name
    last_name VARCHAR(50) UNIQUE,                    -- Variable-length string for last name
    email VARCHAR(100),                       -- Variable-length string for email
    date_of_birth DATE,                       -- Date type for birthdate
    is_active BOOLEAN,                        -- Boolean type for status
    salary DECIMAL(10, 2),                    -- Decimal type for salary with 2 decimal places
    hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp type with default current time
    phone_number CHAR(15),                   - Fixed-length string for phone number
    id INT check(id>1),
    address TEXT                              -- Text type for longer addresses
);

CREATE TABLE employee (
    ID INT,
    Name VARCHAR(30),
    Address VARCHAR(50),
    salary INR
);
    
-- insert
INSERT INTO customers(first_name, last_name, points) VALUES ('Akash', 'edara', default);
INSERT INTO customers(first_name, last_name, points) VALUES ('Akash', 'edara', default),('Akash', 'edara', default);


-- primary key and forigen key
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);


-- update and alter, delete
       
UPDATE employees SET department = 'HR' WHERE last_name = 'Doe';

update employees
SET department = case
                        when id=1 then 'HR'
                        when id=2 then 'abc'
                 end,
     col2 = case
                when id=1 then 10
                when id=2 then 20
            end
where id in (1,2,3);

DELETE FROM employees WHERE last_name = 'Doe';

ALTER TABLE employees ADD col1 VARCHAR(20);

ALTER TABLE employees DROP COLUMN col1;

ALTER TABLE employees MODIFY col1 INT;

-- filter and sort
select * from table1 where col1 = 10;

select * from table1 order by col1 ASC;

select * from table1 order by col2 DESC;

-- TRuncate and drop
TRUNCATE TABLE table1;

DROP TABLE table1;

--condtions
—- AND (both conditions must be True) 
SELECT * FROM customers WHERE birth_date > '1990-01-01' AND points > 1000 

—- OR (at least one condition must be True) 
SELECT *
FROM customers 
WHERE birth_date > ‘1990-01-01’ OR points > 1000 

—- NOT (to negate a condition) 
SELECT *
FROM customers 
WHERE NOT (birthdate > ‘1990-01-01’)


—- Returns customers in any of these states: VA, NY, CA
SELECT *
FROM customers 
WHERE state IN ('VA', 'NY', 'CA');

-- BETWEEN Operator 
SELECT *
FROM customers 
WHERE points BETWEEN 10 AND 1000;

-- like
select *
from customers
where first_name like 'a%';

select *
from customers
where state like 'M_';

-- regxp

select *
from customers
where first_name REGEXP '^a';

select *
from customers
where first_name REGEXP 'ra$|^a';

select *
from customers
where first_name REGEXP 'ac|^a';


select *
from customers
where first_name REGEXP 'i[e]';

-- NULL
select * 
from customers
where phone is NULL;


-- AGG"S and Groupby, HAVING
SELECT COUNT(*) AS total_employees
FROM employees;

SELECT SUM(salary) AS total_salary
FROM employees;

SELECT AVG(salary) AS average_salary
FROM employees;

SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
FROM employees;

select SUM(salary) as total_salary, department from employees group by department;

SELECT salesperson, SUM(amount) AS total_sales FROM sales
GROUP BY salesperson
HAVING SUM(amount > 4000;

--subquery
SELECT employee_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');

-- top and limit
SELECT *
FROM customers 
WHERE customer_id > 5
ORDER BY first_name
LIMIT 3;

select * from customers limit 3, 3;

select top 3 * from employees;
select top 2 * from employees order by salary desc;

-- distinct
select distinct name,id from employees;

--advance select
select 
first_name, last_name, points*10 + 100
from customers;

SELECT first_name, last_name, points, (points * 10 + 20) AS discount_factor
FROM customers;

--colease
select name, COALESCE(col1, "unknown") as col1 from table1;

select name, COALESCE(col1, col2, "unknown") as col1 from table1;

-- order by
select * from customers
order by state DESC;

-- joins
select * from customers, orders;

-- inner
select * from customers c
join
orders o
on c.customer_id = o.customer_id;

select * from customers c INNER JOIN orders o on c.id = o.id;

-- left
SELECT * FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- right
SELECT * FROM customers c RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- outer
SELECT * FROM customers c FULL JOIN orders o ON c.customer_id = o.customer_id;

-- cross
SELECT * FROM customers CROSS JOIN orders;

-- join across dbs
select * from sql_store.order_items oi join sql_inventory.products p on oi.product_id = p.product_id; 

-- self join
select * from employees e join employees m on e.reports_to = m.employee_id;

-- implict joins(no join syntax)
select * from customers c , orders o where c.customer_id = o.customer_id;

-- UNION and UNION ALL
SELECT *
FROM table1
UNION
SELECT *
FROM table2;

SELECT *
FROM table1
UNION ALL
SELECT *
FROM table2;

-- using clause
SELECT *
FROM customers c
JOIN orders o 
 USING (customer_id);

--windows fucntions : advanced analytical queries
--types of windows functions
--agg: max(), min(), sum(), count(), avg()
--ROW_NUMBER(): Assigns a unique number to each row, starting from 1.
RANK(): Similar to ROW_NUMBER() but with the same rank for equal values and leaves gaps in the ranking.
DENSE_RANK(): Similar to RANK(), but it does not leave gaps between ranks.
NTILE(): Divides the result set into a specified number of roughly equal groups.

--find min amount of each region
select *, MIN(col1) OVER(PARTITION BY region) from sales;

select *, ROW_NUMBER() OVER(ORDER BY salary ASC) as RN from employees;

select *, RANK() OVER(ORDER BY salary ASC) as RN from employees;

select *, DENSE_RANK() OVER(ORDER BY salary ASC) as RN from employees;

--lead() and lag(): are used to access the data from the next/previous row.
--lead -> next and lag-> previous

select *, lag(salary) OVER(order by exp) as new_Sal from employess;

--previous to previous
select *, lag(salary,2) OVER(order by exp) as new_Sal from employess; 

select *, lag(salary,2,0) OVER(order by exp) as new_Sal from employess;

select *, lead(salary) OVER(order by exp) as new_Sal from employess;


---CTE: common table expression which will be used to store temporary result

with cte as(select * from employees)
select * from cte;

--views: virtual tables, it does not store data physcially but store the query that generates data.
create view view1 as select col1,col2 from table1;

select * from view1;

drop view view1;

--stored procs
create procedure proc1
as
select * from abc
GO;

exec proc1 ;

create procedure proc2 @id INT
as
select * from table1 where id=@id
GO;

exec proc2 @id=10;


--trigger

CREATE TRIGGER tg1
ON table1
AFTER DELETE
AS
BEGIN
    INSERT INTO backup_table (col1, col2, del_date)
    SELECT 
        col1,
        col2,
        GETDATE()
    FROM deleted;
END;



