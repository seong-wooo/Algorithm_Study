from collections import defaultdict
from collections import deque


def solution(land):
    oil = defaultdict(int)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n = len(land)
    m = len(land[0])
    group = 2

    visited = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                q = deque()
                q.append((y, x))
                visited[y][x] = True
                group += 1

                while q:
                    j, i = q.pop()
                    land[j][i] = group
                    oil[group] += 1

                    for k in range(4):
                        ny = j + dy[k]
                        nx = i + dx[k]

                        if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))

    maximum = 0

    for x in range(m):
        x_total = 0
        s = set()
        for y in range(n):
            add = oil[land[y][x]]

            if add > 0 and land[y][x] not in s:
                s.add(land[y][x])
                x_total += add

        maximum = max(maximum, x_total)

    return maximum







