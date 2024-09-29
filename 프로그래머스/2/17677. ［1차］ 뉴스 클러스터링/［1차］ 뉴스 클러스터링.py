# 교집합크기 / 합집합크기
# 둘 다 공집합일 때 = 1

from collections import Counter

import re
def solution(str1, str2):
    c1 = Counter()
    c2 = Counter()
    
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            c1[str1[i:i+2].upper()] += 1
        
    for j in range(len(str2) - 1):
        if str2[j:j+2].isalpha():
            c2[str2[j:j+2].upper()] += 1
    
    if not c1 and not c2:
        return 65536
    
    return int(sum((c1&c2).values()) / sum((c1|c2).values()) * 65536)
        
    