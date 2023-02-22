import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [a[0]]
maximum = a[0]

for i in range(1, n):
    t = 0
    for j in range(i - 1, -1, -1):
        if a[i] > a[j] and dp[j] > t:
            t = dp[j]

    r = t + a[i]
    dp.append(r)
    if r > maximum:
        maximum = r
print(maximum)

