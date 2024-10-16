-- 코드를 입력하세요
SELECT car_id
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = '세단' and car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                                    where month(START_DATE) = 10 )
order by 1 desc