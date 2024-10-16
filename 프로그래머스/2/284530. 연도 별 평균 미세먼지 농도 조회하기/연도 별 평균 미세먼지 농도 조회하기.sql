-- 코드를 작성해주세요
# 수원 지역
# 연도 별 평균 미세먼지 오염도와 평균 초미세먼지 오염도

select year(YM) YEAR, round(avg(PM_VAL1),2) 'PM10', round(avg(PM_VAL2),2) 'PM2.5'
from AIR_POLLUTION
where LOCATION2 = '수원'
group by 1
order by 1