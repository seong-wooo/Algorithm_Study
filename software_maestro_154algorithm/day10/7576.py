import sys
from collections import deque


def result(box):
    days = 1
    for b in box:
        if 0 in b:
            return "-1"
        days = max(days, max(b))

    return str(days - 1)


m, n = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

q = deque()
for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            q.append((y, x))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while q:
    a, b = q.popleft()

    for i in range(4):
        da = a + dy[i]
        db = b + dx[i]

        if 0 <= da < n and 0 <= db < m and box[da][db] == 0:
            box[da][db] = box[a][b] + 1
            q.append((da, db))

print(result(box))