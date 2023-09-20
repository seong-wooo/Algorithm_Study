import sys

n, k = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))

d = [0 for _ in range(n)]
d[k - 1] += sum(c[:k])

for i in range(k, n):
    d[i] += d[i - 1] + c[i] - c[i - k]


print(max(d[k-1:]))
