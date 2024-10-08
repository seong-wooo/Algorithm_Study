-- 코드를 작성해주세요

select id, length
from (
    select ID, LENGTH
    from FISH_INFO
    order by length desc
    limit 10
) a
order by 2 desc, 1