from collections import defaultdict
def solution(want, number, discount):
    w = defaultdict(int)
    
    for i in range(len(want)):
        w[want[i]] = number[i]
    
    d = defaultdict(int)
    for j in range(10):
        d[discount[j]] += 1
    
    answer = 0 if w != d else 1
    
    for k in range(1, len(discount) - 9):
        d[discount[k-1]] -= 1
        if d[discount[k-1]] == 0:
            del d[discount[k-1]]
        d[discount[k+9]] += 1
       
        if w == d:
            answer += 1
        
        
    return answer