import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    ins = sys.stdin.readline().strip()

    if ins.split()[0] == "push":
        num = ins.split()[1]
        queue.append(num)

    elif ins == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif ins == "size":
        print(len(queue))

    elif ins == "empty":
        if len(queue) == 0 :
            print(1)
        else:
            print(0)

    elif ins == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif ins == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

