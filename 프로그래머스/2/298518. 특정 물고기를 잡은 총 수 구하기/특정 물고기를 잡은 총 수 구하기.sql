-- 코드를 작성해주세요
select count(id) 'FISH_COUNT'
from FISH_INFO
where fish_type in (select fish_type from fish_name_info where fish_name in ('BASS', 'SNAPPER'))