# 시각

# 내가 푼 풀이
# 경우의 수가 매우 적기 때문에 수학적 계산을 통해서 구하였다.
# 시 단위에 3이 들어가는 경우 -> 3 13 23
# 분,초 단위에 3이 들어가는 경우 -> 3,13,23,30~39,43,53  15개

import sys

n = int(sys.stdin.readline())

count = 0
for i in range(n+1):
  if i % 10 == 3:
    count += 60*60
  else:
    count += 15*60 + 15*60 - 15*15


print(count)

# 경우의 수가 적기때문에 완전 탐색으로도 해결 가능
# 물론 내가 푼 풀이가 더 빠르게 동작하지만
# 이 방법 또한 알아둘 것
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count+=1
print(count)