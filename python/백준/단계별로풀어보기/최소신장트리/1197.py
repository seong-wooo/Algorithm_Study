import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

lines = [list(map(int, input().split())) for _ in range(e)]
lines.sort(key=lambda x: x[2])

result = 0
for line in lines:
    a, b, c = line

    if find_parent(a) != find_parent(b):
        union(a, b)
        result += c

print(result)
