-- 코드를 작성해주세요

select hd.DEPT_ID, hd.DEPT_NAME_EN, round(avg(he.sal)) AVG_SAL
from HR_DEPARTMENT hd
inner join
HR_EMPLOYEES he
on hd.dept_id = he.dept_id
group by 1
order by 3 desc