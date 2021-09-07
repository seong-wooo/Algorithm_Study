# 유클리드 호제법을 이용하여 풀었다.
# A,B 의 최소공배수 = A * (B//(A,B의 최대공약수))

import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if b > a:
        a,b = b,a
    A,B = a,b

    while b != 0:
        a,b = b, a%b
    print(A*(B//a))