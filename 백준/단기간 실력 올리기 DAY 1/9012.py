import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    stack = deque()

    vps = sys.stdin.readline().rstrip()

    for ps in vps:
        if ps == "(":
            stack.append(1)
        elif ps == ")" and stack:
            stack.pop()
        else:
            stack.append(1)
            break

    if stack:
        print("NO")
    else:
        print("YES")