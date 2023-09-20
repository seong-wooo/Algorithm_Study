# dictionary를 이용하여 저장한다.
# 알고있던 개념이었지만 쉽게 적용하지 못하였다.
# dictionary에 저장하여 저장된 값은 다시 계산하지 않고 불러오는 방법을 이용했다.
# 이 방법을 생각하지 않고 w() 함수의 규칙이 무엇일지 생각하다가 오랜 시간이 걸렸다.

import sys

def w(a, b, c, d):
    if (a,b,c) in d:
        return d[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            return 1

        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20, d)

        elif a < b and b < c:
            d[(a, b, c)] = w(a, b, c-1, d) + w(a, b-1, c-1, d) - w(a, b-1, c, d)
            return d[(a, b, c)]
        else:
            d[(a, b, c)] = w(a-1, b, c, d) + w(a-1, b-1, c, d) + w(a-1, b, c-1, d) - w(a-1, b-1, c-1, d)
            return d[(a, b, c)]


d = {}

while True:
    x = list(map(int, sys.stdin.readline().split()))
    if x == [-1, -1, -1]:
        break
    print(f"w({x[0]}, {x[1]}, {x[2]}) = {w(x[0],x[1],x[2],d)}")


