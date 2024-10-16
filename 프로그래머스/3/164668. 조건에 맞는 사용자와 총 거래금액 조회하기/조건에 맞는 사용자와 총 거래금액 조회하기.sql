-- 코드를 입력하세요
# status = done
# total_price >= 70

SELECT u.USER_ID, u.NICKNAME, sum(b.price) TOTAL_SALES
from USED_GOODS_USER u
inner join 
USED_GOODS_BOARD b
on b.status = 'DONE' and u.user_id = b.writer_id
group by 1
having TOTAL_SALES >= 700000
order by 3