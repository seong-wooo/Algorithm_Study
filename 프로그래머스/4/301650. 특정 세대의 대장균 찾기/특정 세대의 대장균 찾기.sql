-- 코드를 작성해주세요

with parent as (
    select 
        id 
    from 
        ecoli_data
    where parent_id is null
), child as (
    select 
        id
    from
        ecoli_data
    where parent_id in (select id from parent)
)


select id 
from ecoli_data
where parent_id in (select id from child)
order by 1