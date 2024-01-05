def solution(n):
    one = bin(n)[2:].count("1")
    next = n + 1
    while bin(next)[2:].count("1") != one:
        next+=1
    return next