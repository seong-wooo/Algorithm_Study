from collections import deque
def solution(order):
    stack = deque()
    
    belt = deque([i for i in range(1, len(order) + 1)])
    
    answer = 0
    i = 0
    while i < len(order):
        o = order[i]
        if belt and belt[0] == o:
            belt.popleft()
            i += 1
        elif stack and stack[-1] == o:
            stack.pop()
            i += 1
        else:
            if belt:
                stack.append(belt.popleft())
            else:
                break
        
    return i
        
    
    
    