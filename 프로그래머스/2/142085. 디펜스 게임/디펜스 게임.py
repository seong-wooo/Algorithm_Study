from heapq import heappush, heappop

def solution(n, k, enemy):
    q = []
    current = 0
    
    for i in range(len(enemy)):
        current += enemy[i]
        heappush(q, -enemy[i])
        
        if current > n:
            if k > 0:
                current += heappop(q)
                k -= 1
            else:
                return i
    return len(enemy)