from collections import deque

def solution(s):
    stack = deque()
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
  
    return 0 if stack else 1