from collections import deque

def solution(number, k):
    q = deque()
    
    i = 0
    while k > 0 and i < len(number):
        while q and number[i] > q[-1] and k > 0:
            q.pop()
            k -= 1
        q.append(number[i])
        i += 1
    
    if k == 0:
        return ''.join(q) + ''.join(number[i:])
    
    return ''.join(q)[:-k]