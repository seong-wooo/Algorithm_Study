import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def hasCycle(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

    return False


n, m = map(int, input().split())
parent = [i for i in range(n)]

result = 0
for i in range(m):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)

    if a == b:
        result = i + 1
        break

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

print(result)
