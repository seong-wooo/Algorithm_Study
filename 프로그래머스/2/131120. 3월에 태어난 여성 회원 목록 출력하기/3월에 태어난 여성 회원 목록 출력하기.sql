-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') DATE_OF_BIRTH
from MEMBER_PROFILE
where month(date_of_birth) = 3 and gender = 'W' and TLNO is not null
order by MEMBER_ID