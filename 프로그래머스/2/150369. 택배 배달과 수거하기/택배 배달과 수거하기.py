def solution(cap, n, deliveries, pickups):
    d_end = len(deliveries) - 1
    p_end = len(pickups) - 1
    
    answer = 0
    
    while d_end >= 0 or p_end >= 0:
        round_d = 0
        round_p = 0
        
        while d_end >= 0 and deliveries[d_end] == 0:
            d_end -= 1
        
        move = d_end+1
        
        while p_end >= 0 and pickups[p_end] == 0:
            p_end -= 1
        
        answer += max(move, p_end+1) * 2
        
        while d_end >= 0 and round_d < cap:
            if round_d + deliveries[d_end] <= cap:
                round_d += deliveries[d_end]
                deliveries[d_end] = 0
                d_end -= 1
            else:
                deliveries[d_end] -= cap-round_d
                round_d += cap - round_d
                
        while p_end >= 0 and round_p < cap:
            if round_p + pickups[p_end] <= cap:
                round_p += pickups[p_end]
                pickups[p_end] = 0
                p_end -= 1
            else:
                pickups[p_end] -= cap-round_p
                round_p += cap - round_p
            
    return answer
                
    
    