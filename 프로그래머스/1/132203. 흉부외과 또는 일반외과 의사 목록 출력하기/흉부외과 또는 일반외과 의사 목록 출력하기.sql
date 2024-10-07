-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd,'%Y-%m-%d') HIRE_YMD
from DOCTOR
where MCDP_CD in ('CS', 'GS')
order by HIRE_YMD desc, dr_name