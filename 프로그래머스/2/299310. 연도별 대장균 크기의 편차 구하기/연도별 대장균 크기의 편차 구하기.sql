-- 코드를 작성해주세요

select year(ed.DIFFERENTIATION_DATE) year, m.max_size-ed.size_of_colony 'year_dev', ed.id
from ecoli_data ed

inner join 
(select year(DIFFERENTIATION_DATE) YEAR, max(size_of_colony) 'max_size'
from ecoli_data
group by year(DIFFERENTIATION_DATE)) m
on year(ed.DIFFERENTIATION_DATE) = m.year

order by 1, 2