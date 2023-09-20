# 다음 번에 나올 숫자의 개수 :
# 9의 개수 -> 8의개수
# 8의 개수 -> 7 +9의개수
# 7의 개수 -> 6 + 8의 개수
#...
# 1의 개수 -> 2 + 0의 개수
# 0의 개수 -> 1의개수

# 리스트 하나를 이용해서
# 매 턴마다 각 요소들을 변경한다.

import sys

n = int(sys.stdin.readline())

num= [0] + [1] * 9

for i in range(1, n):
    num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9] \
    = num[1], num[0] + num[2],num[1] + num[3],num[2]+ num[4],num[3] + num[5],num[4] +num[6],num[5] + num[7],num[6] + num[8],num[7] + num[9], num[8]

print(sum(num)%1000000000)

