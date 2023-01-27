import sys
from collections import deque

commend = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]

stack = deque()

for co in commend:

    if "push_front" in co:
        stack.appendleft(int(co.split()[1]))

    elif "push_back" in co:
        stack.append(int(co.split()[1]))

    elif co == "pop_front":
        print(stack.popleft() if stack else -1)

    elif co == "pop_back":
        print(stack.pop() if stack else -1)

    elif co == "size":
        print(len(stack))

    elif co == "empty":
        print(0 if stack else 1)

    elif co == "front":
        print(stack[0] if stack else -1)

    elif co == "back":
        print(stack[-1] if stack else -1)
