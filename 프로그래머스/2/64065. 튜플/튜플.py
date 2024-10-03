import re
from collections import Counter
def solution(s):
    c = Counter()
    
    for x in map(lambda x: x.split(","), re.split("},{", s[2:-2])):
        c += Counter(x)
    
    return list(map(int, sorted(c.keys(), key=lambda x: -c[x])))
    