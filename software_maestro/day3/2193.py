n = int(input())

dp = [[0, 0], [0, 1], [1, 0]]

for i in range(3, n + 1):
    zero, one = dp[i - 1]
    dp.append([one + zero, zero])

print(sum(dp[n]))
