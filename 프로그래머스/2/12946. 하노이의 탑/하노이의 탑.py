def solution(n):
    return hanoi(1, 3, n)
    
def hanoi(a, b, n):
    if n == 1:
        return [[a, b]]
    
    return hanoi(a, 6-a-b, n-1) + hanoi(a, b, 1) + hanoi(6-a-b, b, n-1)
    

    