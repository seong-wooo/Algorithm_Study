-- 코드를 작성해주세요

select count(id) FISH_COUNT, month(time) MONTH
from FISH_INFO
group by 2
order by 2