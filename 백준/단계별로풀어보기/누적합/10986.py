import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a[0] %= m
for i in range(1, n):
    a[i] = (a[i] + a[i - 1]) % m

counter = Counter(a)

result = counter[0]

for c in counter.values():
    result += c * (c - 1) // 2

print(result)