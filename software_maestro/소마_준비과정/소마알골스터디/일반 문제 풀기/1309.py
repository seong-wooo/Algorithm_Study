n = int(input())

dp = [0, 3, 7] + [0] * (n - 2)

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[n])