-- 코드를 입력하세요

-- 트럭
-- 대여 기록 별로 대여 금액 (fee)
-- 대여 금액 내림차순, 대여 기록 ID 내림차순

with truck as (
    select car_id, daily_fee
    from CAR_RENTAL_COMPANY_CAR
    where car_type = '트럭'
), seven as (
    select discount_rate 
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    where DURATION_TYPE = '7일 이상'
        and car_type = '트럭'
), thirty as (
    select discount_rate 
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    where DURATION_TYPE = '30일 이상'
        and car_type = '트럭'
), ninty as (
    select discount_rate 
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    where DURATION_TYPE = '90일 이상'
        and car_type = '트럭'
)


select h.history_id, 
    round(case
        when datediff(h.end_date, h.start_date) + 1 < 7 then (datediff(h.end_date, h.start_date) + 1) * t.daily_fee
        when datediff(h.end_date, h.start_date) + 1 < 30 
        then (datediff(h.end_date, h.start_date) + 1) * t.daily_fee * (1 - (select discount_rate from seven) * 0.01)
        when datediff(h.end_date, h.start_date) + 1 < 90 
        then (datediff(h.end_date, h.start_date) + 1) * t.daily_fee * (1 - (select discount_rate from thirty) * 0.01)
        else (datediff(h.end_date, h.start_date) + 1) * t.daily_fee * (1 - (select discount_rate from ninty) * 0.01)
    end) fee
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
inner join truck t
on h.car_id = t.car_id
order by 2 desc, 1 desc

