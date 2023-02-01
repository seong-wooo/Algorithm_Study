import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def find_child(root):
    for node in tree[root]:
        if parent[node] == 0:
            parent[node] = root
            find_child(node)


parent[1] = 1
find_child(1)

for p in parent[2:]:
    print(p)