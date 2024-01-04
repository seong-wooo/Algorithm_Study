from collections import deque


def solution(s):
    q = deque()
    
    for c in s:
        if q and q[-1] == c:
            q.pop()
        else:
            q.append(c)
    return 1 if not q else 0