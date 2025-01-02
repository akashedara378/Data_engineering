
create database db1;
create database if not exists db1;

drop database if exists db1;
drop database db1;

use database db1;

show databases;
show tables;

CREATE TABLE person (
    person_id INT PRIMARY KEY,                -- Integer type for unique identifier
    first_name VARCHAR(50),                   -- Variable-length string for first name
    last_name VARCHAR(50),                    -- Variable-length string for last name
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
INSERT INTO customers(first_name, last_name, points)
VALUES ('Akash', 'edara', default);

INSERT INTO customers(first_name, last_name, points)
VALUES ('Akash', 'edara', default),
       ('Akash', 'edara', default);
-- primary key anf forigen key
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



       
UPDATE employees
SET department = 'HR'
WHERE last_name = 'Doe';

DELETE FROM employees
WHERE last_name = 'Doe';

SELECT salesperson, SUM(amount) AS total_sales
FROM sales
GROUP BY salesperson
HAVING SUM(amount) > 4000;

-- union
SELECT first_name
FROM customers 
UNION
SELECT name
FROM shippers;

-- union
SELECT first_name
FROM customers 
UNION ALL
SELECT name
FROM shippers;

SELECT employee_name
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');

use sql_store;

SELECT *
FROM customers 
WHERE customer_id > 5
ORDER BY first_name
LIMIT 3;

select 
first_name, last_name, points*10 + 100
from customers;

-- Using expressions
SELECT first_name, last_name, points, (points * 10 + 20) AS discount_factor
FROM customers;

-- Removing duplicates
SELECT DISTINCT state
FROM customers


—- AND (both conditions must be True) 
SELECT *
FROM customers 
WHERE birth_date > '1990-01-01' AND points > 1000 

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

-- order by

select * from customers
order by state DESC;

-- limit
select * from customers limit 3;

select * from customers limit 3, 3;


-- joins
select * from customers, orders;

-- inner
select * from customers c join orders o on c.customer_id = o.customer_id;
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
use sql_store;
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


-- cross
SELECT *
FROM customers 
CROSS JOIN products;

-- union
SELECT first_name
FROM customers 
UNION
SELECT name
FROM shippers;

-- insert
INSERT INTO customers(first_name, last_name, points)
VALUES ('Akash', 'edara', default);

INSERT INTO customers(first_name, last_name, points)
VALUES ('Akash', 'edara', default),
       ('Akash', 'edara', default);


Error Code: 1364. Field 'last_name' doesn't have a default value
