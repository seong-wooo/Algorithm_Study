import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    q = deque()

    q.append((0, 0))

    dy = [0, 1]
    dx = [1, 0]

    while q:
        y, x = q.popleft()

        if y == x == n - 1:
            return "HaruHaru"

        for i in range(2):
            ny = y + dy[i] * maps[y][x]
            nx = x + dx[i] * maps[y][x]

            if  0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))



    return "Hing"


print(bfs())
