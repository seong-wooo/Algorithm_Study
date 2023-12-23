from collections import deque

def solution(queue1, queue2):
    t_q1 = sum(queue1)
    t_q2 = sum(queue2)
    
    if (t_q1 + t_q2) % 2 != 0:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    result = 0
    while q1 and q2 and t_q1 != t_q2 and result < len(queue1) * 4:
        if t_q1 > t_q2:
            p = q1.popleft()
            t_q1 -= p
            t_q2 += p
            q2.append(p)
        else:
            p = q2.popleft()
            t_q1 += p
            t_q2 -= p
            q1.append(p)
        
        result += 1
        
    return result if t_q1 == t_q2 else -1