import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())

while (w, h) != (0, 0):
    ls = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    land = 0
    for y in range(h):
        for x in range(w):
            if ls[y][x]:
                q = deque([(y, x)])
                ls[y][x] = 1
                land += 1

                while q:
                    a, b = q.popleft()
                    for i in range(8):
                        da = a + dy[i]
                        db = b + dx[i]

                        if 0 <= da < h and 0 <= db < w and ls[da][db]:
                            ls[da][db] = 0
                            q.append((da, db))

    print(land)



    w, h = map(int, sys.stdin.readline().split())
