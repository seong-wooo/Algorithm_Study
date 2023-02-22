import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]


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


for i in range(1, n + 1):
    road = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if road[j] == 1:
            union(i, j)


start, *city = list(map(int, input().split()))


def canGo():
    for c in city:
        if find_parent(start) != find_parent(c):
            return False
    return True

print("YES" if canGo() else "NO")


