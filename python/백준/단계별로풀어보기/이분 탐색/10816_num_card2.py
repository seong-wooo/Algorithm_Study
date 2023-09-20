# Counter 메소드를 이용하여 구하였다.
# Counter를 쓰니까 바로 풀리는 문제
# 개수 셀땐 Counter
# Counter를 이용하여 요소별로 개수를 나타내고
# counter안에 있다면 개수 출력 없다면 0출력

import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
c = Counter(a)

m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if i in c:
        print(c[i],end=" ")
    else:
        print(0,end=" ")