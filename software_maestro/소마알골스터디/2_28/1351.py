import sys
sys.setrecursionlimit(10**6)
n, p, q = map(int, sys.stdin.readline().split())

d = dict()
d[0] = 1

def dfs(n):
    if n in d:
        return d[n]

    d[n] = dfs(n // p) + dfs(n // q)
    return d[n]


print(dfs(n))