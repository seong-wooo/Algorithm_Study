import sys
import heapq

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    heapq.heappush(graph[u], v)
    heapq.heappush(graph[v], u)

visited = [False] * (n + 1)

result = [0] * (n + 1)

order = 1
def dfs(graph, visited, r):
    global order
    while graph[r]:
        next = heapq.heappop(graph[r])
        if not visited[next]:
            result[next] = order
            order += 1
            visited[next] = True
            dfs(graph, visited, next)


visited[r] = True
result[r] = order
order += 1
dfs(graph, visited, r)

print("\n".join(map(str, result[1:])))
