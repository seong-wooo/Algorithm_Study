# 11050문제에서 10007로 나누는 것만 추가하였다.

import sys

def bc(n, k):
    total = 1
    for d in range(1, k + 1):
        total *= n
        n -= 1

    for  p in range(1, k+1):
        total //= p
    return total

n, k = map(int, sys.stdin.readline().split())

print(bc(n, k) % 10007)