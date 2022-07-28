import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = [0] * n
result = 0

total = sum(a)

for i in range(n):
    total -= a[i]
    b[i] += a[i] * total

print(sum(b) % 1000000007)