def solution(n, s):
    if s < n:
        return [-1]
    
    c = s // n
    s = s % n
    return [c] * (n - s) + [c+1] * s

    
    
    