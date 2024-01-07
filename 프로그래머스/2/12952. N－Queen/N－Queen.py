# 각 행에 하나씩


def solution(n):

    return queen([], n)
        


def queen(before, n):
    if len(before) == n:
        return 1
    
    current = len(before)
    valid = [1] * n
    for b in before:
        valid[b] = 0

    for i in range(len(before)):
        right = before[i] + current - i
        left = before[i] - current + i
        if right < n:
            valid[right] = 0
        if 0 <= left:
            valid[left] = 0
    
    return sum(queen(before + [i], n) for i in range(len(valid)) if valid[i])
        