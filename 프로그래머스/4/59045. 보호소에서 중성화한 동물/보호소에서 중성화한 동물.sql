-- 코드를 입력하세요
# 중성화 x -> Intact
# 중성화 o -> Spayed | Neutered

SELECT
    animal_id, animal_type, name
from
    animal_ins
where   
    SEX_UPON_INTAKE like 'Intact%'
    and animal_id in (select animal_id from animal_outs where SEX_UPON_OUTCOME regexp 'Spayed|Neutered')
order by 
    1
