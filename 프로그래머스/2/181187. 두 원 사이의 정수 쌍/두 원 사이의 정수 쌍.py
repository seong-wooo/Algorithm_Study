from math import sqrt, ceil

def solution(r1, r2):
    answer = r2 - r1 + 1
    r22 = r2*r2
    r12 = r1*r1
    
    for x in range(1, r1):
        x2 = x*x
        answer += int(sqrt(r22 - x2)) - ceil(sqrt(r12 - x2)) + 1
    
    
    for x in range(r1, r2):
        x2 = x*x
        answer += int(sqrt(r22 - x2))
    
    return answer * 4
        
    
    