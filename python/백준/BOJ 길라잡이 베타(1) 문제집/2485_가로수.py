# 모든 간격들을 구하여
# 그 간격들의 최대 공약수를 구한다.
# 최대 공약수의 간격마다 가로수가 있어야한다.

import math
import sys

n = int(sys.stdin.readline())

a = [int(sys.stdin.readline()) for _ in range(n)]

sub_arr = set()
for i in range(1, n-1):
    if a[i+1] - a[i] not in sub_arr:
        sub_arr.add(a[i+1] - a[i])

gcd = a[1] - a[0]
for s in sub_arr:
    gcd = math.gcd(gcd, s)

result = 0
for j in range(n-1):
    result += (a[j+1] - a[j]) // gcd - 1

print(result)
