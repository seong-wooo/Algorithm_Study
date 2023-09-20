# 상당히 어려운 문제였다.
# x,y,z 세 숫자가 있다고 가정해보자

# x = m * a + r
# y = m * b + r
# z = m * c + r
# r을 없애기 위해서 두 수의 차를 구한다.


# x - y = m(a-b)
# y - z = m(b-c)

# 여기서 m, a-b 는 x-y의 공약수이고 m, b-c는 y-z의 공약수이다.
# x-y 와 y-z의 최대 공약수를 m이라고 하자
# 그러면 이 문제에서 m의 약수를 구한다면
# r의 값이 모두 같을 것이다.

# 최대 공약수를 구하기 위해 math.gcd 함수를 이용하였다.

import sys
import math

n = int(sys.stdin.readline())

a = [int(sys.stdin.readline()) for _ in range(n)]
b = [abs(a[i]-a[i+1]) for i in range(n-1)]
gcd = b[0]
for i in range(1, len(b)):
    gcd = math.gcd(gcd, b[i])

f = [gcd]
for i in range(2,int(gcd**0.5) + 1):
    if gcd % i== 0:
        f.append(i)
        f.append(gcd//i)

f = list(set(f))
f.sort()

for i in f:
    print(i, end= " ")