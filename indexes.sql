-- indexes for faster retrival

CREATE INDEX idx_last_name ON Employees(last_name);


CREATE INDEX idx_last_name ON Employees(first_name, last_name);


DROP INDEX idx_last_name ON Employees;

ALTER TABLE Employees DROP INDEX idx_last_name;


-- stored proc are precompiled, which means the SQL statements within them are parsed and optimized by the database engine before execution.

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT
);

CREATE PROCEDURE GetEmployeeDetails
    @employee_id INT
AS
BEGIN
    SELECT * FROM Employees WHERE employee_id = @employee_id;
END;

EXEC GetEmployeeDetails @employee_id = 101;

-- views : virtual tables only req info from main tabke

create view view1 as
select rollno, name, marks from table1;
select * from view1

Drop view view1

