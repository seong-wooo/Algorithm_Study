from collections import deque

def solution(queue1, queue2):
    t_q1 = sum(queue1)
    t_q2 = sum(queue2)
    total = t_q1 + t_q2
    if total % 2 == 1:
        return -1
    target = total // 2
    
    q = queue1 + queue2
    
    n = len(queue1) + len(queue2)
    start = 0
    end = len(queue1) - 1
    result = 0
    while t_q1 != target:
        if t_q1 > target:
            t_q1 -= q[start]
            start += 1
        
        else:
            end += 1
            if end == n:
                return -1
            
            t_q1 += q[end]
        result += 1
            
    return result
    
