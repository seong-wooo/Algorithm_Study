import re
from collections import Counter

def solution(s):

    c = Counter(re.findall("\d+", s))
    
    return list(map(int, sorted(c.keys(), key = lambda x : c[x], reverse =True)))
    