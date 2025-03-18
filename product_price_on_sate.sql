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
