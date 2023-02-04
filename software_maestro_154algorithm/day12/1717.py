import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a




for _ in range(m):
    x, a, b = map(int, input().split())

    # find
    if x:
        print("YES" if find_parent(parent, a) == find_parent(parent, b) else "NO")


    # union
    else:
        union(parent, a, b)