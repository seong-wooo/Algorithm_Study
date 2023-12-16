from collections import deque

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = deque()
    
    for index, num in enumerate(numbers):
        
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(index);
        
        
    return answer