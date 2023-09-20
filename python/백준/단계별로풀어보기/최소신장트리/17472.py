# 다리는 직선
# 다리 길이 2 이상
# 다리 양 끝은 섬과 인접한 바다

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
island = 2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            while q:
                a, b = q.popleft()
                graph[a][b] = island

                for i in range(4):
                    na = a + dy[i]
                    nb = b + dx[i]

                    if 0 <= na < n and 0 <= nb < m and graph[na][nb] == 1:
                        graph[na][nb] = island
                        q.append((na, nb))
            island += 1

cost_is1_is2 = []

for g in graph:
    j = 0
    start = j
    while j < m:
        if g[j] > 0:
            start = j
            end = start + 1
            while end < m:
                if g[end] > 0:
                    if g[start] == g[end]:
                        start = end
                    else:
                        if end <= start + 2:
                            start = end

                        else:
                            cost_is1_is2.append((end - start - 1, g[start], g[end]))
                            break
                end += 1
            j = end
        else:
            j += 1

for j in range(m):
    i = 0
    start = i
    while i < n:
        if graph[i][j] > 0:
            start = i
            end = start + 1
            while end < n:
                if graph[end][j] > 0:
                    if graph[start][j] == graph[end][j]:
                        start = end

                    else:
                        if end <= start + 2:
                            start = end

                        else:
                            cost_is1_is2.append((end - start - 1, graph[start][j], graph[end][j]))
                            break
                end += 1
            i = end
        else:
            i += 1

parent = [0, 0] + [i for i in range(2, island)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


cost_is1_is2.sort()

result = 0
cnt = 0
for cii in cost_is1_is2:
    cost, is1, is2 = cii

    if find_parent(is1) != find_parent(is2):
        union(is1, is2)
        result += cost
        cnt += 1
        if cnt == n - 1:
            break

print(result if len(set(find_parent(x) for x in range(2, len(parent)))) == 1 else -1)
