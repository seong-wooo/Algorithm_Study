import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
y, x = map(int, input().split())

target = list(tuple(map(int, input().split())) for _ in range(m))
target_count = 0
moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

visited = [[0] * (n + 1) for _ in range(n + 1)]

q = deque([(y, x, 1)])
visited[y][x] = 1

while q:
    y, x, count = q.popleft()
    count += 1

    for dy, dx in moves:
        ny, nx = y + dy, x + dx

        if 1 <= ny < n + 1 and 1 <= nx < n + 1 and not visited[ny][nx]:
            visited[ny][nx] = count
            q.append((ny, nx, count))


print(*map(lambda x: visited[x[0]][x[1]] - 1, target))
