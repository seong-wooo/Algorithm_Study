import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited_dfs = [False] * (n + 1)
visited_bfs = visited_dfs[:]

result = deque()


def dfs(graph, v):
    if not visited_dfs[v]:
        result.append(v)
        visited_dfs[v] = True

        for i in range(1, n + 1):
            if graph[v][i]:
                dfs(graph, i)


def bfs(graph, v):
    result = deque()
    result.append(v)

    q = deque()
    q.append(v)
    visited_bfs[v] = True

    while q:
        front = q.popleft()

        for i in range(1, n + 1):
            if graph[front][i]:
                if not visited_bfs[i]:
                    q.append(i)
                    result.append(i)
                    visited_bfs[i] = True
    return result

dfs(graph, v)
print(*result)
print(*bfs(graph, v))
