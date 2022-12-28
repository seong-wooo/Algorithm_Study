# 문제의 난이도가 과대평가됨
# 큰 값의 돈을 먼저 낼 수록 적은 동전 개수를 낼 수 있다.

import sys

n, k = map(int, sys.stdin.readline().split())

a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

coin_count = 0

for i in range(n-1, -1 , -1):
    if a[i] > k:
        continue
    else:
        coin_count += int(k/a[i])
        k %= a[i]
        if k == 0:
            break

print(coin_count)