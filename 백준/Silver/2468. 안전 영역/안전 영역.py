import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]
max_height = 1
for j in range(n):
    for i in range(n):
        max_height = max(max_height, area[j][i])

answer = 1
for h in range(1, max_height):
    result = 0
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if area[j][i] > h and not visited[j][i]:
                result += 1
                q = deque()
                visited[j][i] = True
                q.append((j, i))

                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and area[ny][nx] > h:
                            visited[ny][nx] = True
                            q.append((ny, nx))
    answer = max(result, answer)
print(answer)






