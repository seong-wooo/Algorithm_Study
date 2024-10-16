-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, a.PT_NO, a.MCDP_CD,	d.DR_NAME,	a.APNT_YMD
from APPOINTMENT a
inner join
    PATIENT p
on 
    p.pt_no = a.pt_no
inner join
    doctor d
on
    a.MDDR_ID = d.DR_ID
where 
    a.MCDP_CD = 'CS' and 
    a.APNT_CNCL_YMD is null and 
    date_format(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13'

order by a.APNT_YMD