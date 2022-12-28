# [n+1][k+1] 크기의 2차원 배열을 이용한다.
# i번째 물건을 챙길때 vs 안챙길 때의 최댓값을 구한다.
# 내가 처음 쓴 코드는 O(n^2)이었다면 이 코드는 O(n)이다.
# MAX 비교를 한번만 해도되니까 ..
# 이 코드는 물건을 챙기느냐 안챙기느냐에 초점을 맞췄다.
# 처음 쓴 코드는 각 무게의 최댓값을 모두 비교하느라 시간초과


import sys

n, k = map(int, sys.stdin.readline().split())

wv = [[0,0]]

for i in range(1, n+1):
  wv.append(list(map(int,sys.stdin.readline().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1, k+1):
    if j >= wv[i][0]:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-wv[i][0] ] + wv[i][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][k])

# 내가 처음 쓴 코드
# 이 코드는 시간 초과에 걸렸다.

# import sys
#
# n, k = map(int, sys.stdin.readline().split())
#
# wv = {}
#
# for i in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     wv[w] = v
#
# # i 무게를 가지고 간다고할 때
# # [i-j] +[j] 의 최댓값을 구한다
#
# dp = [0] * (k + 1)
#
# for i in range(k + 1):
#     if i in wv:
#         dp[i] = wv[i]
#     for j in range(i // 2 + 1):
#         dp[i] = max(dp[i], dp[i - j] + dp[j])
#
# print(dp[k])
