#토마토
# bfs를 진행하면 차례대로 1칸씩 증가한다.
# 이를 이용한다.

import sys
from collections import deque


m,n = map(int, sys.stdin.readline().split())

graph =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]


queue = deque()

for j in range(n):
  for i in range(m):
    if graph[j][i] == 1:
      queue.append((j,i))

dx = [0,0,1,-1]
dy = [1,-1,0,0]


# 굳이  if graph[ny][nx] == 0: 에
# 추가로 graph[ny][nx] > graph[y][x] + 1 을 넣을필요없음
# 원래 더 크다.
while queue:
  y,x = queue.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < m and 0<= ny < n:
        if graph[ny][nx] == 0:
          graph[ny][nx] = graph[y][x] + 1
          queue.append((ny,nx))

days = 0
for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit()
  days = max(days, max(i))

print(days-1)