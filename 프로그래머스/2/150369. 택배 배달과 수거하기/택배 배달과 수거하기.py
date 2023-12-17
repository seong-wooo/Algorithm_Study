def solution(cap, n, deliveries, pickups):        
    d = n - 1
    p = n - 1
    
    while d >= 0 and deliveries[d] == 0:
        d -= 1
    
    while p >= 0 and pickups[p] == 0:
        p -= 1
        
    
    answer = 0
    while d >= 0 or p >= 0:
        start_d = d
        start_p = p
        answer += (start_d + 1) * 2 if start_d > start_p else (start_p + 1) * 2
        
        c = cap
        while d >= 0 and (c > 0 or deliveries[d] == 0):
            if deliveries[d] > c:
                deliveries[d] -= c
                c = 0
                
            else:
                c -= deliveries[d]
                deliveries[d] = 0
                d -= 1
                
        
        c = cap
        while p >= 0 and (c > 0 or pickups[p] == 0):
            if pickups[p] > c:
                pickups[p] -= c
                c = 0
                
            else:
                c -= pickups[p]
                pickups[p] = 0
                p -= 1
    
    return answer