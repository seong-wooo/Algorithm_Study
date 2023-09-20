import heapq
import sys
from math import sqrt
from heapq import heappop

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


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

god = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

e = 0
for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(a) != find_parent(b):
        union(a, b)
        e += 1
if e == n - 1:
    print("0")
else:
    lines = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            xi, yi = god[i]
            xj, yj = god[j]
            lines.append((sqrt((xi - xj) ** 2 + (yi - yj) ** 2), i, j))

    heapq.heapify(lines)
    result = 0

    while e < n - 1:
        cost, a, b = heappop(lines)
        if find_parent(a) != find_parent(b):
            union(a, b)
            result += cost
            e += 1

    print("{:.2f}".format(result))
