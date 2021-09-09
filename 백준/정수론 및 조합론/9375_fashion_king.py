# 옷을 입는 경우는 다음과 같다
# (종류1의 개수 + 1) * (종류2의 개수 + 1) * ... (종류 n의 개수 + 1) - 1
# 위와 같이 계산한 이유:
# 한 종류1을 입게 되는 경우의 수는 종류1의 개수 + 1이다.
# 여기서 +1 은 종류1을 안입게 될 때의 경우의 수다
# 그리고 마지막 항 -1 의 의미는 모든 종류의 옷을 안입게 되는 경우를 경우의 수에서 제외한 것이다.
# 각 종류의 개수는 Counter 클래스를 이용하여 구현하였다.

import sys
from collections import Counter

t = int(sys.stdin.readline())

for i in range(t):
    clothes = []
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
    else:
        for j in range(n):
            clothes.append(sys.stdin.readline().split()[1])

        c = list(Counter(clothes).values())

        days = 1

        for i in range(len(c)):
            days *= 1 + c[i]

        print(days - 1)