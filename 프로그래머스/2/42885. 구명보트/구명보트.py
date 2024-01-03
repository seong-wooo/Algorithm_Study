from collections import deque

def solution(people, limit):
    q = deque(sorted(people, reverse = True))
    
    answer = 0
    while q:
        big = q.popleft()
        
        if q and big + q[-1] <= limit:
            q.pop()
        answer += 1
        
    return answer