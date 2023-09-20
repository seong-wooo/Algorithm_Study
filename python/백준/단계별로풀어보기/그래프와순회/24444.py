import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

q = deque()
visited = [False] * (n + 1)
q.append(r)
visited[r] = True
result = [0] * (n + 1)
order = 1
result[r] = order
order += 1

while q:
    node = q.popleft()

    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            q.append(next)
            result[next] = order
            order += 1


print("\n".join(map(str, result[1:])))
