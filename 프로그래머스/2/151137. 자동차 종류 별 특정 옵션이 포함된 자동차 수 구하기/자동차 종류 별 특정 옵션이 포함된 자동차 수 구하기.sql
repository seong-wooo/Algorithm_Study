-- 코드를 입력하세요
SELECT CAR_TYPE, count(car_id) CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS regexp '통풍시트|열선시트|가죽시트'
group by 1
order by 1