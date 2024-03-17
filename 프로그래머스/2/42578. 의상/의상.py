from collections import defaultdict
def solution(clothes):
    d = defaultdict(int)
    
    for c in clothes:
        d[c[1]] += 1
    
    answer = 1
    for v in d.values():
        answer *= v + 1
    
    return answer - 1
    