# 배수, 약수의 개념을 알고있다면 쉽게 풀 수 있는 문제

import sys
while True:
    a, b = map(int, sys.stdin.readline().split())

    if (a,b) == (0,0):
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
