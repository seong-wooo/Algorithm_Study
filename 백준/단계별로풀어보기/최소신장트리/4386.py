import math
import sys
from math import sqrt

sys.setrecursionlimit(10 ** 6)


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


input = sys.stdin.readline
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
lines = []
for i in range(n):
    for j in range(i + 1, n):
        x_i, y_i = stars[i]
        x_j, y_j = stars[j]
        lines.append((sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2), i, j))

lines.sort()
result = 0
for line in lines:
    cost, a, b = line

    if find_parent(a) != find_parent(b):
        result += cost
        union(a, b)
print(round(result, 2))