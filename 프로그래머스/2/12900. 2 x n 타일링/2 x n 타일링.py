def solution(n):
    a = 1
    b = 2
    
    for i in range(3, n + 1):
        a, b = b, (a + b) % 1000000007
    
    return b