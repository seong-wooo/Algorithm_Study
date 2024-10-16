-- 코드를 입력하세요
SELECT
    product_code, sum(p.price * o.sales_amount) price
from
    product p
inner join
    OFFLINE_SALE o
on
    p.product_id = o.product_id
group by
    p.product_code
order by 
    2 desc, 1