import sys

input = sys.stdin.readline
n, m = map(int,input().split())
a = [0] + list(map(int, input().split()))
for i in range(2, n + 1):
    a[i] += a[i - 1]

count = 0

start = 0
end = 1

while end <= n:
    if a[end] - a[start] == m:
        count += 1
        start += 1
        end += 1
        continue

    if a[end] - a[start] > m:
        start += 1
    else:
        end += 1



print(count)
