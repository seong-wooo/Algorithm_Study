from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    
    d = [defaultdict(int) for _ in range(course[-1] + 1)]
    
    for order in orders:
        for c in course:
            if c <= len(order):
                for a in combinations(sorted(list(order)), c):
                    d[c][a] += 1
    
    answer =[]
    for c in course:
        if d[c]:
            max_val = max(d[c].values())
            if max_val >= 2:
                answer += ["".join(k) for k in d[c].keys() if d[c][k] == max_val]
    
    return sorted(answer)
        
        


        
        