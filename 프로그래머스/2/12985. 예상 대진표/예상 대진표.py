def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)
    
    while a % 2 != 1 or b % 2 != 0 or a + 1 != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
        
    return answer
