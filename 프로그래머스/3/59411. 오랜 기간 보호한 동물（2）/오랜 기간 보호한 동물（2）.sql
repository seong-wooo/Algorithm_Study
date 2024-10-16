-- 코드를 입력하세요
SELECT i.ANIMAL_ID	,i.NAME
from ANIMAL_INS i
inner join
ANIMAL_OUTS o
on i.animal_id = o.animal_id
order by datediff(o.datetime, i.DATETIME) desc
limit 2
