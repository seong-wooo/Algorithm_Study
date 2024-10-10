-- 코드를 입력하세요
select p.product_code, p.price * os.total_amount `sales`
from product p 
inner join 
(select product_id, sum(sales_amount) `total_amount` from offline_sale group by product_id) os
on p.product_id = os.product_id
order by 2 desc, 1