import sys
from collections import deque

ps = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]

for p in ps:
    stack = deque()
    result = True
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(1)
        else:
            if not stack:
                result = False
                break
            stack.pop()

    if stack or not result:
        print("NO")
    else:
        print("YES")


