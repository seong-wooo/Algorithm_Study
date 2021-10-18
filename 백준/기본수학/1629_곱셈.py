# 엄청 헤맸지만 결국 아는 문제였다.
# (a^n) % c  = ((a%c)^n) % c 임을 이용하면 된다.

# a =int(a/c) * c  +a%c
# a*a = (int(a/c) * c)^2 + 2*int(a/c) * b + (a%c)^2
# -> a*a 에서 앞 두항은 c로 나눠짐 -> 볼 필요 없음
# 따라서 우리는 a%c에 대해서만 c보다 큰 지 확인하면 된다.

# 알게 된 사실 : pow(a,b,c) 하면 밑의 코드와 같음

import sys

a, b, c = map(int, sys.stdin.readline().split())

def pow_a(a,b):
    if b == 1:
        return a%c
    if b%2 == 0:
        return pow(pow_a(a,b//2),2)%c
    else:
        return (a *pow( pow_a(a,b//2),2)) % c

print(pow_a(a,b))
