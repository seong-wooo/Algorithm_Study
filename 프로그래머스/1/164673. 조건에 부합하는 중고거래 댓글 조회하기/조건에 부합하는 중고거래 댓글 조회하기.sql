-- 코드를 입력하세요
SELECT gb.title, gb.board_id, gr.reply_id, gr.writer_id, gr.contents, date_format(gr.created_date, '%Y-%m-%d') created_date
from USED_GOODS_BOARD gb
inner join USED_GOODS_REPLY gr on gb.board_id = gr.BOARD_ID
where date_format(gb.created_date, '%Y-%m') = '2022-10'
order by 6, 1