
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
