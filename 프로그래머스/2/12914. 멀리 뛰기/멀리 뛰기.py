def solution(n):
    a, b = 1, 2
    
    for _ in range(n-1):
        a, b = b, (a+b) % 1234567
    
    return a