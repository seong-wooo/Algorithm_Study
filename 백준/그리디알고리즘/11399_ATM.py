# 간단하게 구하면 리스트를 정렬하고
# 총합에 모든 인덱스에 대해서 인덱스의 값 * (n -인덱스) 들을 더해준다

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
total = 0
for i in range(n):
    total += (n-i) * p[i]
print(total)