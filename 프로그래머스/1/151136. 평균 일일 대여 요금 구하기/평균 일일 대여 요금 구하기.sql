-- 코드를 입력하세요
# SELECT round(average(daily_fee)) 'AVERAGE_FEE'
select round(avg(daily_fee))
from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'