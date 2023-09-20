import sys

n, m = map(int, sys.stdin.readline().split())
a = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, len(a)):
    a[i] += a[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(a[j] - a[i - 1])
