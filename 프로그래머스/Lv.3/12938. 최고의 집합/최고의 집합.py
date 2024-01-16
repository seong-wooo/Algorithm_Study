def solution(n, s):
    if s < n:
        return [-1]
    
    c = s // n
    result = [c] * n
    s = s % n
    
    j = n - 1
    while s > 0:
        result[j] += 1
        j -= 1
        s -= 1
        
    return result
    
    