import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

result = 0
for i in range(1, n + 1):
    if not visited[i]:
        q = deque([i])
        visited[i] = True

        while q:
            popleft = q.popleft()
            for v in graph[popleft]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
        result += 1


print(result)
