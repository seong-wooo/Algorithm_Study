import sys
from math import gcd

for _ in range(int(sys.stdin.readline())):
    n, *a = map(int, sys.stdin.readline().split())
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            result += gcd(a[i], a[j])
    print(result)