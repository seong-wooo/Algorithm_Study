# 7576문제에서 z 항목을 추가하면 된다.
# 추가로 마지막 출력 부분에서 시간 초과가 갈렸다.
# 출력을 할 때 큰 단위로 쪼개서 출력하자
# 인덱스 하나하나 조회하다간 시간초과난다.

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

graph = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(h)]

queue = deque()

for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 1:
                queue.append((k, j, i))

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz,ny,nx))

days = 0


for k in graph:
    for j in k:
        for i in j:
            if i == 0:
                print(-1)
                exit(0)
        days = max(days, max(j))

print(days - 1)