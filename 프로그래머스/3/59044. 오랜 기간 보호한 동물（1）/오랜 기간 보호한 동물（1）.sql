-- 코드를 입력하세요
-- 입양 못간 애
-- 가장 오래 있던 3마리

SELECT
    name, datetime
from 
    animal_ins
where
    animal_id not in (select animal_id from animal_outs)
order by
    datetime
limit 3
    