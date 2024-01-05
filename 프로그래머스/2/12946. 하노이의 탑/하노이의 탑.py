def solution(n):
    answer = []
    hanoi(1, 3, n, answer)
    
    return answer
    
def hanoi(a, b, n, answer):
    if n == 1:
        answer.append([a, b])
        return
    
    hanoi(a, 6-a-b, n-1, answer)
    hanoi(a, b, 1, answer)
    hanoi(6-a-b, b, n-1, answer)
    

    