# 이전에 풀었던 문제라 빠르게 점화식을 세울 수 있었다.
n = int(input())
dp = [0,1,2]
for i in range(3,n+1):
    dp.append((dp[i-2] + dp[i-1]))
print(dp[n] % 10007)