from collections import deque

def solution(numbers):
    answer = [-1] * len(numbers)
    q = deque()
    for i in range(len(numbers)):    
        while q and q[-1][0] < numbers[i]:
            value, index = q.pop()
            answer[index] = numbers[i]
        
        q.append((numbers[i], i))
    
    return answer