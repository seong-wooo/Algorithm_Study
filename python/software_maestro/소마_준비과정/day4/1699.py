import math

n = int(input())
dp = [n] * (n + 1)

for i in range(1, n + 1):
    if math.sqrt(i) % 1 == 0:
        dp[i] = 1
    else:
        for j in range(1, int(math.sqrt(i))):
            jj = j ** 2
            dp[i] = min(dp[i], dp[jj] + dp[i - jj])
            if dp[i] == 2:
                break

print(dp[n])