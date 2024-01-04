from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    
    for c in clothes:
        d[c[1]].append(c[0])
        
    answer = 1
    for v in d.values():
        answer *= len(v) + 1
        
    return answer - 1
        
