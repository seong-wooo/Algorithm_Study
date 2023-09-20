# 1로 만들기

x = int(input())
dp = [0,0] + (x-1)*[0]

for i in range(2, x+1):
  minimum = dp[i-1] + 1
  if i % 5 == 0:
    minimum = min(minimum, dp[i//5]+1)
  if i % 3 == 0:
    minimum = min(minimum, dp[i//3]+1)
  if i % 2 == 0:
    minimum = min(minimum, dp[i//2]+1)
  dp[i] = minimum

print(dㅇ[x])