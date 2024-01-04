from collections import deque


def solution(prices):
    stack = deque()
    
    answer = [0] * len(prices)
    
    for i, x in enumerate(prices):
        while stack and stack[-1][0] > x:
            bx, bi = stack.pop()
            answer[bi] = i - bi
        stack.append((x, i))
    
    for x, i in stack: 
        answer[i] = len(prices) - i - 1
        
    return answer
                
