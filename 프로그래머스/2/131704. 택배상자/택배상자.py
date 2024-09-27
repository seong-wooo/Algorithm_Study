from collections import deque

def solution(order):
    q = deque([i for i in range(1, len(order) + 1)])
    bozo_q = deque()
    
    answer = 0 
    for i in range(len(order)):
        if bozo_q and bozo_q[-1] == order[i]:
            bozo_q.pop()
            answer += 1
            continue
        
        while q and q[0] != order[i]:
            bozo_q.append(q.popleft())
            
        if q and q[0] == order[i]:
            q.popleft()
            answer += 1
        
        else:
            break
    
    return answer        