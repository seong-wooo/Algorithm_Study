import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in a:
    print(*i)