def solution(n):
    target = bin(n).count("1")
    n += 1
    
    while bin(n).count("1") != target:
        n += 1
    
    return n
    