import sys
from collections import deque

left = deque(sys.stdin.readline().rstrip())
right = deque()

for i in range(int(sys.stdin.readline())):
    commend = sys.stdin.readline().rstrip()

    if commend == "L":
        if left:
            right.appendleft(left.pop())

    elif commend == "D":
        if right:
            left.append(right.popleft())

    elif commend == "B":
        if left:
            left.pop()

    else:
        left.append(commend.split()[1])

print("".join(left) + "".join(right))
