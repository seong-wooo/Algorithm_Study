from collections import Counter

def solution(clothes):
    c = Counter([k for c, k in clothes])
        
    answer = 1
    for v in c.values():
        answer *= v + 1
        
    return answer - 1
        
