-- 코드를 입력하세요
#  2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수

with joined as (
    select user_id
    from user_info
    where year(joined) = 2021
)

select year(sales_date) 'year', 
        month(sales_date) 'month',
        count(distinct user_id) 'purchased_users',
        round(count(distinct user_id)/(select count(user_id) from joined), 1) PUCHASED_RATIO
from online_sale
where user_id in (select user_id from joined)

group by 
1,2

order by
1, 2