from collections import defaultdict


def solution(str1, str2):
    d1 = split(str1)    
    d2 = split(str2)
    
    if not d1 and not d2:
        return 65536
        
    k1 = set(d1.keys())  
    k2 = set(d2.keys())  
    
    inters, union = k1&k2, k1|k2
    
    return (65536 * sum([min(d1[k],d2[k]) for k in inters])) // sum(max(d1[k], d2[k]) for k in union)
    
    
    
def split(str):
    d = defaultdict(int)
    
    for i in range(len(str) - 1):
        target = str[i:i+2]
        if target.isalpha():
            d[target.upper()] += 1
    
    return d