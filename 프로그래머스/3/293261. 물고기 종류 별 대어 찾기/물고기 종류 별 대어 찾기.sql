select fi.id, fni.fish_name, fi.length
from fish_info fi
inner join 

(select fish_type, max(length) max_length
from fish_info
group by fish_type) m
on fi.fish_type = m.fish_type and fi.length = m.max_length

inner join
fish_name_info fni 
on fi.fish_type=fni.fish_type

order by 1