import sys
from collections import deque

commend = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]

stack = deque()

for co in commend:

    if "push" in co:
        stack.append(int(co.split()[1]))

    elif co == "pop":
        print(stack.pop() if stack else -1)

    elif co == "size":
        print(len(stack))

    elif co == "empty":
        print(0 if stack else 1)

    elif co == "top":
        print(stack[-1] if stack else -1)
