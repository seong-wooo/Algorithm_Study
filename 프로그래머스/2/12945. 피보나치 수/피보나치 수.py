def solution(n):
    a = 1
    b = 1
    
    for _ in range(n-1):
        a, b = b, (a+b) % 1234567
        
    
    return a