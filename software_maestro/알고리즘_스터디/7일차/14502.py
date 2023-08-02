import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

safe_zones = []

for j in range(n):
    for i in range(m):
        if not graph[j][i]:
            safe_zones.append((j, i))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def calcSafeZone(w1, w2, w3):
    copy_grpah = deepcopy(graph)
    y1, x1 = w1
    y2, x2 = w2
    y3, x3 = w3

    copy_grpah[y1][x1] = 1
    copy_grpah[y2][x2] = 1
    copy_grpah[y3][x3] = 1

    q = deque()

    for j in range(n):
        for i in range(m):
            if copy_grpah[j][i] == 2:
                q.append((j, i))

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m and not copy_grpah[ny][nx]:
                copy_grpah[ny][nx] = 2
                q.append((ny, nx))


    result = 0
    for j in range(n):
        for i in range(m):
            if not copy_grpah[j][i]:
                result += 1

    return result


result = 0
for w1, w2, w3 in combinations(safe_zones, 3):
    result = max(result, calcSafeZone(w1, w2, w3))

print(result)
