-- 코드를 작성해주세요

select ii.item_id, ii.item_name
from ITEM_INFO ii
inner join item_tree it
on ii.item_id = it.item_id
where parent_item_id is null