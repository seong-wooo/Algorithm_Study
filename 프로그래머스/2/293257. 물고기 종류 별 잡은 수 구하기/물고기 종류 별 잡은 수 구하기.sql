-- 코드를 작성해주세요

select count(i.id) fish_count, n.fish_name
from FISH_INFO i 
inner join fish_name_info n
on i.fish_type = n.fish_type
group by 2
order by 1 desc