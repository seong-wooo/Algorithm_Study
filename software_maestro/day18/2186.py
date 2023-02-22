import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

a = [input().rstrip() for _ in range(n)]

target = input().rstrip()

q = deque()

for j in range(n):
    for i in range(m):
        if a[j][i] == target[0]:
            q.append((j, i, 0))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]
result = 0
while q:
    y, x, index = q.popleft()

    if index == len(target) - 1:
        result += 1
        continue

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == target[index + 1]:
            q.append((ny, nx, index + 1))

print(result)
