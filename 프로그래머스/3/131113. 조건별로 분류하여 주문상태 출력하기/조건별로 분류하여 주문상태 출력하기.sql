-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') out_date, 
    case
        when OUT_DATE is NULL then '출고미정'
        when date_format(OUT_DATE, '%Y-%m-%d') <= '2022-05-01' then '출고완료'
        else '출고대기'
    end
'출고여부'
from FOOD_ORDER
order by 1 