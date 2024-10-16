-- 코드를 입력하세요
SELECT 
HISTORY_ID, car_id, date_format(START_DATE,'%Y-%m-%d') start_date, date_format(END_DATE,'%Y-%m-%d') end_date, 
    case 
        when datediff(end_date, start_date) + 1>= 30 then '장기 대여'
        else '단기 대여'
    end  RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(START_DATE, '%Y-%m') = '2022-09'
order by 1 desc