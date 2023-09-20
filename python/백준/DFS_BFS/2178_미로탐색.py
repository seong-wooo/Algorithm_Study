# 이 코드가 가장 빨랐다.
# 나는 queue 를 deque을 사용하여 구현하였지만
# 이 코드에서는 list를 사용하였다.
# 또한 굳이 1과 0을 int로 바꿀 필요가 없다.

import sys

n, m = map(int, sys.stdin.readline().split())

graph =[sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]

queue = [(0,0)]
visited[0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]


while queue:
  y,x = queue.pop(0)
  if x == m-1 and y ==n-1:
    break
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < m and 0<= ny < n:
      if graph[ny][nx] == "1" and visited[ny][nx] == 0:
        visited[ny][nx] = visited[y][x] + 1
        queue.append((ny,nx))

print(visited[n-1][m-1])