import re
from collections import Counter

def solution(s):
    c = Counter(re.findall('\d+', s))
    
    return [int(k) for k, v in sorted(c.items(), key = lambda x: -x[1])]
    