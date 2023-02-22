import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

miro = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(a)]
visited = [[False] * b for _ in range(a)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

q = deque([(0, 0)])
visited[0][0] = True

while q:
    y, x = q.popleft()

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy < a and 0 <= xx < b and not visited[yy][xx] and miro[yy][xx] == 1:
            q.append((yy, xx))
            visited[yy][xx] = True
            miro[yy][xx] = miro[y][x] + 1

    if miro[a - 1][b - 1] != 1:
        break

print(miro[a - 1][b - 1])


