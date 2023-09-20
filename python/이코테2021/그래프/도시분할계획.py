import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)


parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

path = []
for i in range(m):
    a, b, cost = map(int, input().split())
    path.append((cost, a, b))

path.sort()

result = []
for i in path:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))