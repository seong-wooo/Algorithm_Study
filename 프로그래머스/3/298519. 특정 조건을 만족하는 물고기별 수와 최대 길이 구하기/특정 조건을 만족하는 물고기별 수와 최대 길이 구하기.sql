-- 코드를 작성해주세요

select count(id) FISH_COUNT, max(length) MAX_LENGTH, FISH_TYPE
from FISH_INFO
group by 3
having avg(coalesce(length, 10)) >= 33
order by 3