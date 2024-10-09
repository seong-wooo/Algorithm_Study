-- 코드를 작성해주세요
with recursive no_child as (
    select 
        id, 1 as generation 
    from
        ecoli_data
    where parent_id is null
    
    union all
    
    select
        ed.id, generation + 1
    from 
        ecoli_data ed
    inner join no_child nc on nc.id = ed.parent_id
    where generation < (select count(id) from ECOLI_DATA)
)

select count(id) count, generation 
from no_child
where id not in (select parent_id from ecoli_data where parent_id is not null)
group by generation
order by 2