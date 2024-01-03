from collections import deque

def solution(number, k):
    stack = deque()
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    return "".join(stack) if k == 0 else "".join(list(stack)[:-k])
            
