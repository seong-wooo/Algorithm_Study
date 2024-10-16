-- 코드를 작성해주세요

with front_end_code as (
    select code from skillcodes where category = 'Front End'    
)


select 
    id, email, first_name, last_name
from
    DEVELOPERS d
where 
    exists (select code from front_end_code where code&d.skill_code = code)

order by
    1   