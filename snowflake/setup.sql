use role accountadmin;

use warehouse war1;

create or replace database db;

create or replace schema Schema1;

use database db;

use schema Schema1;


create or replace table perm_table(
ID int,
value string
);

alter table perm_table set data_retention_time_in_days=10;

create or replace transient table trans_table(
ID int,
value string
);


create or replace temporary table temp_table(
ID int,
value string
);


show tables;


-- views

CREATE OR REPLACE TABLE employee (
    emp_id      INT,
    first_name  STRING,
    last_name   STRING,
    department  STRING,
    salary      NUMBER,
    hire_date   DATE
);


INSERT INTO employee VALUES
(1, 'Alice', 'Smith', 'HR',        60000, '2020-01-15'),
(2, 'Bob',   'Jones', 'IT',        80000, '2019-03-22'),
(3, 'Carol', 'Davis', 'Finance',   75000, '2021-06-10'),
(4, 'Dave',  'Miller','IT',        85000, '2022-11-01'),
(5, 'Eve',   'Wilson','Marketing', 70000, '2023-05-18');


CREATE OR REPLACE VIEW vw_all_employees AS
SELECT * FROM employee;

-- Usage
SELECT * FROM vw_all_employees;


CREATE OR REPLACE VIEW vw_avg_salary_by_dept AS
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department;

select * from vw_avg_salary_by_dept order by avg_salary desc;



CREATE OR REPLACE materialized VIEW mt_vw_avg_salary_by_dept AS
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department;


select * from mt_vw_avg_salary_by_dept order by avg_salary desc;






