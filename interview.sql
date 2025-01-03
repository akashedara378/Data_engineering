
select distinct * from Employee;

with cte as(
      SELECT *, ROW_NUMBER() over(partition by employee_id order by employee_id) as RN
      from Employee
)

select * from cte where RN=2;

select position,MAX(salary) from Employee
group by position;

select * from Employee order by salary desc limit 3;
---only for sql server
--- select top 3 * from Employee order by salary desc;

--with cte
with cte1 as(
      select distinct * from Employee
)
select * from cte1 order by salary desc limit 3;

---
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    location VARCHAR(50)
);

INSERT INTO Employee (employee_id, employee_name, department, salary, location)
VALUES 
(1, 'Alice Johnson', 'Engineering', 75000, 'New York'),
(2, 'Bob Smith', 'Data Science', 85000, 'San Francisco'),
(3, 'Carol White', 'Human Resources', 65000, 'Chicago'),
(4, 'David Brown', 'Engineering', 78000, 'Austin'),
(5, 'Eva Green', 'Marketing', 70000, 'Seattle'),
(6, 'Frank Martin', 'Data Science', 82000, 'New York'),
(7, 'Grace Lee', 'Finance', 90000, 'Los Angeles'),
(8, 'Harry Clark', 'Sales', 72000, 'Chicago'),
(9, 'Ivy Baker', 'Human Resources', 67000, 'Austin'),
(10, 'Jack Wilson', 'Marketing', 71000, 'San Francisco'),
(11, 'Karen Evans', 'Engineering', 76000, 'Seattle'),
(12, 'Leo Adams', 'Data Science', 84000, 'New York'),
(13, 'Mona Scott', 'Finance', 88000, 'Los Angeles'),
(14, 'Nate Perry', 'Sales', 74000, 'Chicago'),
(15, 'Olivia Cooper', 'Engineering', 78000, 'Austin');
---
with cte as(
select *, DENSE_RANK() OVER(order by salary DESC) as rn from Employee
)
select MIN(salary), department_id from Employee group by department_id;

---
with cte1 as(      
select *, row_number() OVER(partition by department_id order by salary DESC) as row1 from Employee
)
select * from cte1 where row1=2;

---
with cte as(
select *, row_number() over(partition by location order by salary asc) as rn from Employee
)
select * from cte where rn in (1,2);

---
with cte as(
select *, row_number() over(partition by department order by salary desc) as rn from Employee
)
select * from cte where rn in (1,2);

create table table1(
id int
);

Insert into table1 values(1),(1),(1),(1),(1);

create table table2(
id int
);
Insert into table2 values(1),(1),(1),(1),(1),(null);

select count(*) from table1, table2;

---30
select count(*)
from table1 as t1
inner join table2 as t2 
on t1.id=t2.id;

--25
select count(*)
from table1 as t1
left join table2 as t2 
on t1.id=t2.id;

--26
select count(*)
from table1 as t1
right join table2 as t2 
on t1.id=t2.id;

--- full join not there in mysql we can union right join and left join
select *
from table1 as t1
full join table2 as t2 
on t1.id=t2.id;
