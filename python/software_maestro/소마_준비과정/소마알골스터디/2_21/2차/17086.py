import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for j in range(n):
    for i in range(m):
        if s[j][i] == 1:
           q.append((j, i))

dy = [0, 0, 1, 1, 1, -1, -1, -1]
dx = [1,-1, 0, -1, 1, 0, -1, 1]

while q:
    y, x = q.popleft()

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and not s[ny][nx]:
            s[ny][nx] = s[y][x] + 1
            q.append((ny, nx))

mx = 0
for l in s:
    mx = max(mx, max(l))


print(mx - 1)