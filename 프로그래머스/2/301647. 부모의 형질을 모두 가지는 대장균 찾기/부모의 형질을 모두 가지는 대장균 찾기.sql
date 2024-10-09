-- 코드를 작성해주세요

select ed1.id, ed1.genotype, ed2.genotype 'parent_genotype'
from ECOLI_DATA ed1
inner join ECOLI_DATA ed2 on ed1.parent_id = ed2.id
where ed1.genotype&ed2.genotype=ed2.genotype
order by 1