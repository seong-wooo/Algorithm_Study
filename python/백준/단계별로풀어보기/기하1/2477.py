import sys
from collections import deque

k = int(sys.stdin.readline())

d = deque()

for i in range(6):

    d.append(tuple(map(int, sys.stdin.readline().split())))


while True:
    if d[0][0] == d[2][0] and d[1][0] == d[3][0]:
        print(k * (d[4][1] * d[5][1] - d[1][1] * d[2][1]))
        break
    else:
        d.append(d.popleft())
