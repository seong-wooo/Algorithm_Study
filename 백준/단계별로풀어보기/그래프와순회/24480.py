import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

visited = [False] * (n + 1)
count = 1
result = [0] * (n + 1)


def dfs(x):
    global count
    result[x] = count
    count += 1
    visited[x] = True

    for next in graph[x]:
        if not visited[next]:
            dfs(next)


dfs(r)
print("\n".join(map(str, result[1:])))

