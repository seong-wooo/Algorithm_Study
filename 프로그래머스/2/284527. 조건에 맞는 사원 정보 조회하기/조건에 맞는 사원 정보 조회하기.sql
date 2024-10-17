with max_score as (
    select emp_no, sum(score) 'score'
    from HR_GRADE
    where year = 2022
    group by emp_no
)

select m.SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from max_score m
inner join
HR_EMPLOYEES e
on m.emp_no = e.emp_no
where score = (select max(score) from max_score)
