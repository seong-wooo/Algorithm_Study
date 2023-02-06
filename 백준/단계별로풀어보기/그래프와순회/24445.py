import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
visited = [0] * (n + 1)
q.append(r)
order = 1
visited[r] = order
order += 1

while q:
    node = q.popleft()
    graph[node].sort(reverse=True)
    for next in graph[node]:
        if not visited[next]:
            visited[next] = order
            order += 1
            q.append(next)


print("\n".join(map(str, visited[1:])))
