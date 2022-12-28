# 한바퀴에 2 pi r
# 고로 반지름이 몇 배차이나는가
# 근데 기약 분수 형태로
# 따라서 두 수 사이에 최대 공약수 구하기
# 유클리드 호제법을 이용하여 최대 공약수를 구하고
# 그 수로 나누어 기약 분수를 나타냈다.


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b ,a%b)

import sys

n = int(sys.stdin.readline())

r = list(map(int, sys.stdin.readline().split()))

for i in range(1,n):
    big_r, small_r = r[0], r[i]
    big_fac = gcd(big_r,small_r)
    print(f"{r[0]//big_fac}/{r[i]//big_fac}")