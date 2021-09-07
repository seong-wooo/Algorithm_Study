# 기본적인 수학을 사용하는 방법이었다.
# 유클리드 호제법으로도 풀어보자

import sys

a,b = map(int, sys.stdin.readline().split())
A,B = a,b
if b >= a:
    a,b =b,a

while b != 0:
    a,b = b, a%b

print(a)
print(A * (B//a))

