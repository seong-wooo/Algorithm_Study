-- 코드를 입력하세요
# 중고 거래 게시물을 3건 이상 등록한 사용자
# 
SELECT USER_ID, NICKNAME, concat(city, ' ', STREET_ADDRESS1,' '	,STREET_ADDRESS2) '전체주소',
concat(substring(TLNO, 1, 3), '-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4)) '전화번호'
from USED_GOODS_USER
where USER_ID in 
    (select WRITER_ID from USED_GOODS_BOARD group by writer_id having count(BOARD_ID) >=3 )
order by 1 desc