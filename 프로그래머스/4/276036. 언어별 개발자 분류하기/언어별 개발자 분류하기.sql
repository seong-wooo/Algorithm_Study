-- 코드를 작성해주세요

with frontend as (
    select sum(code) code
    from SKILLCODES
    where category = 'Front End'
), python as (
   select code
    from SKILLCODES
    where name = 'Python' 
), cs as (
       select code
    from SKILLCODES
    where name = 'C#' 
)

select 
    case
        when d.skill_code & (select code from frontend)
            and d.skill_code & (select code from python)
        then 'A'
        when d.skill_code & (select code from cs)
        then 'B'
        when d.skill_code & (select code from frontend) 
        then 'C'
        else 'D'
    end 

GRADE, d.ID, d.EMAIL
from DEVELOPERS d
group by 1,2,3
having grade != 'D'
order by 1, 2