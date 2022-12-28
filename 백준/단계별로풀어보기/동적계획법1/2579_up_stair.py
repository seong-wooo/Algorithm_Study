# dp 리스트에 인덱스마다 가질 수 있는 최댓값을 저장
# 저장할때는 (3번째 전 + 1번째 전) 과 2번째 전 인덱스의 크기를 비교해야한다.

import sys

n = int(sys.stdin.readline())


s =[]
for i in range(n):
    s.append(int(sys.stdin.readline()))
if n == 1:
    print(s[0])

elif n == 2:
    print(s[0] + s[1])
else:
    dp = []

    dp.append(s[0])
    dp.append(max(s[0] + s[1], s[1]))
    dp.append(max(s[0]+s[2], s[1]+s[2]))

    for i in range(3, n):
        dp.append(max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i]))

    print(dp[-1])




