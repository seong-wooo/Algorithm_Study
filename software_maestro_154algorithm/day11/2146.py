import sys
from collections import deque

n = int(sys.stdin.readline())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
if n == 1:
    print(1 - land[0][0])
    exit(0)

visited = [[0] * n for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

qq = deque()
group = 1
for y in range(n):
    for x in range(n):
        if land[y][x] and not visited[y][x]:
            q = deque([(y, x)])
            qq.append((y, x))
            visited[y][x] = group

            while q:
                a, b = q.popleft()
                for i in range(4):
                    da = a + dy[i]
                    db = b + dx[i]
                    if 0 <= da < n and 0 <= db < n and land[da][db] and not visited[da][db]:
                        visited[da][db] = group
                        q.append((da, db))
                        qq.append((da, db))

            group += 1

def bfs():
    result = sys.maxsize
    while qq:
        a, b = qq.popleft()

        for i in range(4):
            da = a + dy[i]
            db = b + dx[i]
            if 0 <= da < n and 0 <= db < n:
                if not land[da][db]:
                    visited[da][db] = visited[a][b]
                    land[da][db] = land[a][b] + 1
                    qq.append((da, db))

                elif visited[da][db] != visited[a][b]:
                    result = min(result, land[da][db] + land[a][b] - 2)
    return result

print(bfs())

