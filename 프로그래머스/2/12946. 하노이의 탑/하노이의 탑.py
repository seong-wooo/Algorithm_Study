def solution(n):
    answer = []
    
    
    hanoi(n, 1, 3, answer)
    
    return answer

def hanoi(n, a, b, answer):
    if n == 1:
        answer.append([a,b])
        return
    
    hanoi(n-1, a, 6-a-b, answer)
    hanoi(1, a, b, answer)
    hanoi(n-1,6-a-b,b, answer)