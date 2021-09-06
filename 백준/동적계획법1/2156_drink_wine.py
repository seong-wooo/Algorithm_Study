# 2579번과 매우 흡사한 문제
# 차이점은 두칸 이상 안마실 수 있다는 것
# 차이점이 제일 중요했다
# 3칸 이상 안마시는 것은 의미가 없다
# 2칸 까지는 안마시는 것이 의미가 있다
# 예를 들어 [100, 100, 1, 1, 100, 100]이 있다고 가정하면
# 1,1 은 스킵하는 것이 베스트이다
# 따라서 dp[2] ,dp[3]  은 dp[1] 값이 이어지는 것이 베스트다


import sys

n = int(sys.stdin.readline())

w = []
dp = [0]*n
for i in range(n):
    w.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(w[:n]))
else:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i], dp[i-1])
    print(dp[-1])
