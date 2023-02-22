import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())

tree = [[] for _ in range(v + 1)]
for _ in range(v):
    node, *e = map(int, input().split())
    i = 0
    while e[i] != -1:
        tree[node].append((e[i], e[i + 1]))
        i += 2


visited = [0] * (v + 1)


def find_dfs(node):
    dist = visited[node]
    for n in tree[node]:
        linked_node, cost = n
        if not visited[linked_node]:
            visited[linked_node] = dist + cost
            find_dfs(linked_node)

visited[1] = 1
find_dfs(1)

maximum = 1
next_node = 1
for i in range(2, v + 1):
    if visited[i] > maximum:
        next_node = i
        maximum = visited[i]

visited = [0] * (v + 1)
visited[next_node] = 1
find_dfs(next_node)
print(max(visited) - 1)
