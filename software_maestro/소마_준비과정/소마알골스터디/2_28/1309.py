n = int(input())

# 넣는 경우, 안 넣는 경우
dp = [[0] * n for _ in range(2)]
dp[0][0], dp[1][0] = 2, 1


for i in range(1, n):
    dp[0][i], dp[1][i]  = (dp[0][i - 1] + dp[1][i - 1] * 2)  % 9901, (dp[0][i-1] + dp[1][i-1])  % 9901

print((dp[0][-1] + dp[1][-1]) % 9901)