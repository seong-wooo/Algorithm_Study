import sys

dp = [0, 1, 2, 4]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    length = len(dp)

    if length > n:
        print(dp[n])
    else:
        for i in range(length, n + 1):
            dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
        print(dp[n])
