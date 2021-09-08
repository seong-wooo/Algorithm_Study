# nCk -> n!/((n-k)!(k)!) 임을 알면 쉽게 구할 수 있다.
# math.factorial을 쓸 수도 있다.

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
print(bc(n,k))


