# 답안 예시

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 내가 쓴 코드
# 틀렸음
# import sys

# n, m = map(int, sys.stdin.readline().split())


# coins =[]
# dp = [-1] * (m+1)


# for i in range(n):
#   coins.append(int(sys.stdin.readline()))

# coins.sort()

# for i in coins:
#   if i <= m:
#     dp[i] = 1

# for won in range(coins[0]+1, m+1):
#   min_coin = 10001
#   for c in coins:
#     if dp[won-c] > 0:
#       min_coin = min(min_coin, dp[won - c] + 1)
#   if min_coin != 10001:
#     dp[won] = min_coin

# print(dp[m])
