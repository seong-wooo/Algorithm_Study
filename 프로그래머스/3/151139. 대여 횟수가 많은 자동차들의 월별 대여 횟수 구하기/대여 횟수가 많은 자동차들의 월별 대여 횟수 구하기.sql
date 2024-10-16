-- 코드를 입력하세요
# 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차


select month(start_date) MONTH, CAR_ID, count(HISTORY_ID) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in(
    SELECT car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
    group by car_id
    having count(car_id) >= 5
) and date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
group by 1, 2 
having count(HISTORY_ID) > 0 
order by 1, 2 desc