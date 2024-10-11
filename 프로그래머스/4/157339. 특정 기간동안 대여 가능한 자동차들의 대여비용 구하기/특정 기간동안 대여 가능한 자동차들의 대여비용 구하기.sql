-- 코드를 입력하세요
with cannot_borrow as (
    select 
        car_id
    from
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where
        date_format(start_date, '%Y-%m-%d') <= '2022-11-31' and
        date_format(end_date, '%Y-%m-%d') >= '2022-11-01' 
), car as (
    select
        *
    from 
        car_rental_company_car
    where
        car_type in ('세단', 'SUV')
), plan as (
    select 
        *
    from 
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where
        DURATION_TYPE = '30일 이상'
)   


SELECT 
    c.car_id, c.car_type, round(30*c.daily_fee*(1-0.01*p.DISCOUNT_RATE)) fee
from 
    car c
inner join
    plan p
on
    c.car_type = p.car_type
where 
    c.car_id not in (select car_id from cannot_borrow)
group by
    c.car_id
having
     500000 <= fee and fee < 2000000
    
order by 3 desc, 2, 1 desc