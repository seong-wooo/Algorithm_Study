import heapq

def solution(n, k, enemy):
    
    q = []
    
    for i in range(len(enemy)):
        if k > 0:
            heapq.heappush(q, enemy[i])
            k -= 1
            continue

        if n < q[0] and n < enemy[i]:
            return i 
        
        if q[0] < enemy[i]:
            n -= heapq.heappop(q)
            heapq.heappush(q, enemy[i])
            
        else:
            n -= enemy[i]
    
    return len(enemy)