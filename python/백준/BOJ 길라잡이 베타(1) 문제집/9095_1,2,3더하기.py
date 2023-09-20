# 점화식을 찾지 못하였다.

# https://blog.sungmin.dev/99
# 위의 블로그에 점화식을 세우는 과정이 잘 나와있다.
# dp[i] = dp[i-1]+dp[i-2]+dp[i-3] 이다.
# 다이나믹프로그래밍 문제가 나오면 점화식을 세우는 것을 연습해보자

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [1, 2, 4]
    for i in range(3, n):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    print(dp[n - 1])