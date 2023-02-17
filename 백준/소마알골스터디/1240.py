import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph2 = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    graph2[a][b] = c
    graph2[b][a] = c


def dfs(a, target):
    if a == target or graph2[a][target] > 0:
        return graph2[a][target]

    for link in graph[a]:
        next, cost = link
        if not visited[next]:
            if graph2[next][target] > 0:
                return graph2[a][next] + graph2[next][target]

            visited[next] = True
            cost = dfs(next, target)

            if cost > 0:
                graph2[next][target] = cost
                return graph2[a][next] + cost

    return -1


for i in range(m):
    a, b = map(int, input().split())
    visited = [False] * (n + 1)
    visited[a] = True

    print(dfs(a, b))