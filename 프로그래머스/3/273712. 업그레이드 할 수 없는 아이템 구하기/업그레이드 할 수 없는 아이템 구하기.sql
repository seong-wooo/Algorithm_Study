-- 코드를 작성해주세요

with recursive item as (
    select parent_item_id
    from item_tree
    where parent_item_id is not null
    
    union
    
    select it.parent_item_id
    from item_tree it
    inner join item 
    on item.parent_item_id = it.item_id
)


select item_id, item_name, rarity
from item_info
where item_id not in (select parent_item_id from item where parent_item_id is not null)
order by 1 desc
