-- 코드를 입력하세요

with recursive hours as (
    select 0 hour
    union all
    select hour + 1
    from hours
    where hour < 23
)

select h.hour, coalesce(a.c, 0) COUNT
from hours h
left outer join
    (select hour(datetime) hour, count(animal_id) c from ANIMAL_OUTS group by 1) a
on h.hour = a.hour
