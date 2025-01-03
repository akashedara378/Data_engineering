
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


--schema
create table table1 as
select * from Employee
where 1=2;
select * from table1;

--data
create table table2 as
select * from Employee
where 1=1;
select * from table2;

--- not supported in mysql
select * into table1 from Employee where 1=2;
select * from table1;

select * from Employee where employee_name like "A%";

select month(current_timestamp);
select year(current_timestamp);
select day(current_timestamp);

--- not on mysql
select getdate();

--- not on mysql
select * from Employee for xml auto;

--- first and last char same
select * from Employee where left(department,1)=right(department,1);

--- first two and last two char same
select * from Employee where left(department,2)=right(department,2);

---

CREATE TABLE Chocolate_Brands (
    chocolate_name VARCHAR(50),
    brand_name VARCHAR(50)
);

INSERT INTO Chocolate_Brands (chocolate_name, brand_name) VALUES
('KitKat', 'Nestle'),
('Perk', NULL),
('Munch', NULL),
('Dairy Milk', 'Cadbury'),
('5 Star', NULL),
('Silk', NULL);


with cte as(
select *, row_number() over(order by(select not null)) as rn,
case when brand_name is not null then 1 else 0 end rn1 
from Chocolate_Brands
), cte1 as(
select *, sum(rn1) over(order by rn) roll_sum from cte
), cte2 as(
select chocolate_name, brand_name, max(brand_name) over(partition by roll_sum) as new_brand from cte1
)


update Chocolate_Brands cb 
join cte2 c2 
on cb.chocolate_name=c2.chocolate_name
set cb.brand_name=c2.new_brand;

select * from Chocolate_Brands;

---
create table customer_orders (
order_id integer,
customer_id integer,
order_date date,
order_amount integer
);

insert into customer_orders values(1,100,cast('2022-01-01' as date),2000),(2,200,cast('2022-01-01' as date),2500),(3,300,cast('2022-01-01' as date),2100)
,(4,100,cast('2022-01-02' as date),2000),(5,400,cast('2022-01-02' as date),2200),(6,500,cast('2022-01-02' as date),2700)
,(7,100,cast('2022-01-03' as date),3000),(8,400,cast('2022-01-03' as date),1000),(9,600,cast('2022-01-03' as date),3000);




with first_vist as(
select customer_id, min(order_date) as first_vist from customer_orders group by customer_id
)

select t2.*, t1.first_vist,
case when t2.order_date=t1.first_vist then 'new' else "repeated" end as customer_type
from first_vist t1
inner join customer_orders t2
on t1.customer_id=t2.customer_id;
