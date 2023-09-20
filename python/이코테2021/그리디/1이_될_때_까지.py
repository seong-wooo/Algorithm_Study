# 1이 될 때까지

# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 1 2 3 4 5 2


# 다이나믹 프로그래밍으로 구현한다.
# dp 리스트에서 k로 나눠질때와 안나눠질때를 구분한다.
# i번째 숫자를 삽입한다고 할 때
# dp[i/k] + 1 과 dp[i-1] + 1 을 비교하여 작은 값을 삽입한다.

# 내가 쓴 풀이
# 이 풀이는 dynamic 프로그래밍으로 해결하였다.
import sys

n, k = map(int, sys.stdin.readline().split())

# 1번 인덱스부터 시작
dp = [0, 0]

# 2번 인덱스부터 삽입
for i in range(2, n + 1):
    # i가 k로 나눠질 때
    if i % k == 0:
        min_count = min(dp[i - 1], dp[i // 5])
        dp.append(min_count + 1)
    # 안나눠질 때
    else:
        dp.append(dp[i - 1] + 1)

print(dp[-1])


# 그리디 알고리즘으로 해결한 풀이

# k가 2이상이라면 1을 빼는 것 보다 k로 나눠주는 것이 항상 더 빠르게 감소한다.
# 따라서 나눠주는 연산을 많이 실행할 수록
# 더 적은 연산 횟수를 가지게 된다.
# 나눠주는 것을 우선시하여 연산하는 것이 포인트

import sys

n, k = map(int,sys.stdin.readline().split())

count = 0
while True:
  target = (n//k) * k
  count += n - target
  n = target
  if n < k:
    break
  while n % k == 0:
    n //= k
    count += 1

count += n - 1
print(count)