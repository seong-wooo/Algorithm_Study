import sys
import math


def z(x, max_k):
    while x <= max_k:
        if x % n == y % n:
            return x
        x += m
    return -1


input = sys.stdin.readline

for i in range(int(input())):
    m, n, x, y = map(int, input().split())
    max_k = m * n // math.gcd(m, n)

    if y > x:
        m, n = n, m
        x, y = y, x

    print(z(x, max_k))




