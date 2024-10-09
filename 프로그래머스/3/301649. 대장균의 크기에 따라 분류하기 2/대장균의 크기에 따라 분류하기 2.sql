select ed.id, 
case
    when oed.ranking = 1 then 'CRITICAL'
    when oed.ranking = 2 then 'HIGH'
    when oed.ranking = 3 then 'MEDIUM'
    when oed.ranking = 4 then 'LOW'
end COLONY_NAME
from ecoli_data ed
inner join (select id, ntile(4) over (order by size_of_colony desc) ranking from ecoli_data) oed
on ed.id = oed.id