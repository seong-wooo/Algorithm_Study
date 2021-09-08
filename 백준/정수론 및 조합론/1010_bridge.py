# m개의 다리 중 n개를 고른다 그러면 순서대로 왼쪽 다리와 짝을 맞추면 된다.
# mCn을 구하는 문제

import sys


def c(n, k):
    total = 1
    for d in range(1, k + 1):
        total *= n
        n -= 1

    for  p in range(1, k+1):
        total //= p
    return total


t = int(sys.stdin.readline())
nm =[]
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(c(m, n))
