import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))

d = [0, p[1]] + [0] * (n - 1)

for i in range(2, n + 1):
    d[i] = p[i]
    for j in range(1, i // 2 + 1):
        d[i] = max(d[i], d[j] + d[i - j])

print(d[n])
