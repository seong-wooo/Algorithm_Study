import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def find_parents(x):
    if parent[x] != x:
        parent[x] = find_parents(parent[x])

    return parent[x]


def union(a, b):
    a = find_parents(a)
    b = find_parents(b)

    if a != b:
        parent[a] = b
        count[b] += count[a]

    return b

for _ in range(int(input())):
    f = int(input())
    parent = {}
    count = {}
    result = []
    for _ in range(f):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = f1
            count[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            count[f2] = 1

        root = union(f1, f2)

        result.append(count[find_parents(root)])
    print("\n".join(map(str,result)))