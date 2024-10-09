-- 코드를 작성해주세요
select parent_id id, count(id) child_count
from ECOLI_DATA
group by parent_id
having parent_id is not null

union all

select id, 0
from ECOLI_DATA
where id not in (select distinct(parent_id) from ECOLI_DATA where parent_id is not null)

order by 1