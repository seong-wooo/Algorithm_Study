import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    maps = [list(map(int, input().split())) for _ in range(h)]

    land = 0
    q = deque()

    for j in range(h):
        for i in range(w):
            if maps[j][i]:
                land += 1
                maps[j][i] = 0
                q.append((j, i))

                while q:
                    y, x = q.popleft()

                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= ny < h and 0 <= nx < w and maps[ny][nx]:
                            maps[ny][nx] = 0
                            q.append((ny, nx))

    print(land)

