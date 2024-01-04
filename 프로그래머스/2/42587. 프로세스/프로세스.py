import heapq as hq
from collections import deque

def solution(p, l):
    a = [-x for x in p]
    
    hq.heapify(a)

    p = deque([(x, i) for i, x in enumerate(p)])
    
    answer = 1
    while p:
        if p[0][0] == -a[0]:
            t = p.popleft()
            if t[1] == l:
                return answer
            hq.heappop(a)
            answer += 1
        else:
            p.append(p.popleft())
    
    return answer