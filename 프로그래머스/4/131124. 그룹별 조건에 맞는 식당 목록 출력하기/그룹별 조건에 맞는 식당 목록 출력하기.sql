-- 코드를 입력하세요
# 리뷰 가장 많이 작성한 회원의 리뷰들

with review as (
    select member_id
    from rest_review
    group by member_id
    order by count(member_id) desc
    limit 1
)


SELECT 
    m.MEMBER_NAME, r.REVIEW_TEXT, date_format(r.REVIEW_DATE, '%Y-%m-%d')
from 
    member_profile m

inner join
    REST_REVIEW r
on
    m.member_id = ( 
        select member_id
        from rest_review
        group by member_id
        order by count(review_id) desc
        limit 1
    )
    and m.member_id = r.member_id

order by
    3, 2
    