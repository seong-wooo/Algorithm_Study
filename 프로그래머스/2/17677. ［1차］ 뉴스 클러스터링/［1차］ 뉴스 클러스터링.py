from collections import defaultdict


def solution(str1, str2):
    d1 = split(str1)    
    d2 = split(str2)
    
    if not d1 and not d2:
        return 65536
        
    union = 0
    inters = 0
    
    for k in d1:
        if k in d2:
            inters += min(d1[k], d2[k])
            d2[k] = max(d1[k], d2[k])
        else:
            union += d1[k]
    
    union += sum(d2.values())
    return (65536 * inters) // union
    
    
    
    
def split(str):
    d = defaultdict(int)
    
    for i in range(len(str) - 1):
        target = str[i:i+2]
        if target.isalpha():
            d[target.upper()] += 1
    
    return d