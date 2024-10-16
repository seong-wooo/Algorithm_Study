-- 코드를 입력하세요
select 
    fh.flavor
from 
    first_half fh
inner join
    july j
on
    fh.flavor = j.flavor
group by 
    1
order by sum(fh.total_order) + sum(j.total_order) desc 
limit 3

