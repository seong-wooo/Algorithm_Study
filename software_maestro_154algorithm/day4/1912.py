import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [a[0]] + [0] * (n - 1)

maximum = a[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i - 1] + a[i])
    maximum = max(maximum, dp[i])

print(maximum)