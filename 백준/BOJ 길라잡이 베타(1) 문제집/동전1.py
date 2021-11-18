import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k+1)

dp[0]=1

# 각 동전별로 따로 계산을 진행한다.
# i번째에 c의 동전을 추가한다고 가정하면 dp[i-c] 개의 경우가 존재한다. 
for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])


