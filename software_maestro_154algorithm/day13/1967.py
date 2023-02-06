import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

visited = [0] * (n + 1)

def dfs(node):
    dist = visited[node]
    for n in tree[node]:
        next, cost = n
        if not visited[next]:
            visited[next] = dist + cost
            dfs(next)

visited[1] = 1
dfs(1)

maximum = 1
far_node = 1
for i in range(2, n + 1):
    if visited[i] > maximum:
        maximum = visited[i]
        far_node = i

visited = [0] * (n + 1)
visited[far_node] = 1
dfs(far_node)

print(max(visited) - 1)
