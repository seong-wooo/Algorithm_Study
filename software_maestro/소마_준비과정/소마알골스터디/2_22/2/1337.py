import sys

input = sys.stdin.readline
n = int(input())

a = sorted(int(input()) for _ in range(n))

min_count = 4
for i in range(n):
    count = len(set(j for j in range(a[i], a[i] + 5)) & set(a[i:i+5]))
    min_count = min(min_count, 5 - count)

print(min_count)