from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    
    for cloth, t in clothes:
        d[t].append(cloth)
    
    
    answer = 1
    for t in d:
        answer *= len(d[t]) + 1
        
    return answer - 1