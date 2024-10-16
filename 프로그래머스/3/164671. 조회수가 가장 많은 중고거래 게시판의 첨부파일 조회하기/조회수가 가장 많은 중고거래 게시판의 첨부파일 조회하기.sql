-- 코드를 입력하세요
#  조회수가 가장 높은 게시물에 대한 첨부 파일 경로 조회

with most_views as (
    select board_id
    from USED_GOODS_BOARD
    where views = (select max(views) from USED_GOODS_BOARD)
)

select concat('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) 'FILE_PATH'
from USED_GOODS_FILE
where board_id = (select board_id from most_views)
order by FILE_ID desc