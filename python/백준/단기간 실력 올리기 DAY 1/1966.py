import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))

    seq = 1

    while True:

        if len(queue) == 1:
            break

        elif queue[0] >= max(list(queue)[1:]):
            queue.popleft()
            m -= 1
            if m < 0:
                break
            else:
                seq += 1

        else:
            queue.append(queue.popleft())

            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1

    print(seq)
