import sys
import heapq

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


while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break

    parent = [i for i in range(m)]
    xyz = [list(map(int, input().split())) for _ in range(n)]
    xyz.sort(key=lambda x: x[2])

    result = 0
    total = 0
    for x, y, cost in xyz:
        total += cost
        if find_parent(x) != find_parent(y):
            result += cost
            union(x, y)
    print(total - result)
