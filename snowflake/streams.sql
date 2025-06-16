show tables;

CREATE OR REPLACE TABLE employee1 (
  emp_id INT,
  first_name STRING,
  last_name STRING,
  department STRING,
  salary NUMBER,
  hire_date DATE
);


INSERT INTO employee1 VALUES
  (1, 'Alice', 'Smith', 'HR', 60000, '2020-01-15'),
  (2, 'Bob', 'Jones', 'IT', 80000, '2019-03-22');


CREATE OR REPLACE STREAM employee_stream ON TABLE employee1;

INSERT INTO employee1 VALUES (3, 'Carol', 'Davis', 'Finance', 75000, '2021-06-10');

SELECT * FROM employee_stream;

UPDATE employee1 SET salary = 85000 WHERE emp_id = 2;

SELECT * FROM employee_stream;

-- DROP STREAM IF EXISTS employee_stream;


-- Append only streams
CREATE OR REPLACE STREAM employee_append_stream 
  ON TABLE employee1
  APPEND_ONLY = TRUE;

INSERT INTO employee1 VALUES (3, 'Carol', 'Davis', 'Finance', 75000, '2021-06-10');

select * from employee_append_stream;

UPDATE employee SET salary = 85000 WHERE emp_id = 2;

DELETE FROM employee WHERE emp_id = 1;

-- Insert only for external tables
CREATE OR REPLACE STREAM ext_events_stream 
ON TABLE ext_table 
APPEND_ONLY = TRUE;

