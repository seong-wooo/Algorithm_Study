import bisect

def solution(c):
    c.sort()
    
    left = 0
    right = c[-1]
    answer = 0
    while left <= right:
        h = (left + right) // 2
        h_count = len(c) - bisect.bisect_left(c, h) # h번 이상 인용된 횟수
        if h_count >= h:
            left = h + 1
            answer = h
        
        else:
            right = h - 1
    
    return answer
            
        
        
    
    