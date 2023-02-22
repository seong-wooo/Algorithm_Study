import sys
from math import factorial

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n) * factorial(m - n)))