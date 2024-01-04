import math
from collections import deque


def solution(progresses, speeds):

    p = deque(math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses)))

    answer = []
    while p:
        result = 1
        d = p.popleft()
        
        while p and d >= p[0]:
            p.popleft()
            result += 1
        answer.append(result)
        
    return answer
        
    
