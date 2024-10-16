-- 코드를 입력하세요
SELECT truncate(price, -4) PRICE_GROUP, count(product_id) PRODUCTS
from product
group by 1
order by 1