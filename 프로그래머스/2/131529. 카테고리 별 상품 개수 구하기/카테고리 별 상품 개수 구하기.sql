-- 코드를 입력하세요
SELECT substring(PRODUCT_CODE, 1, 2) CATEGORY,	count(PRODUCT_ID) PRODUCTS
from PRODUCT
group by 1
order by 1 