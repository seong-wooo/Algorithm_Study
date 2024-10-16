-- 코드를 입력하세요
SELECT b.CATEGORY, sum(bs.SALES) TOTAL_SALES
from book b
inner join book_sales bs
on b.book_id = bs.book_id
where date_format(bs.SALES_DATE, '%Y-%m') = '2022-01'
group by 1
order by 1