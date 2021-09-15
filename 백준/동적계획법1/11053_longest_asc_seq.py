# 현재 인덱스와 그 전 인덱스들과 모두 비교하여
# 전 인덱스보다 클 때 순서의 크기에 따라
# 순서를 바꿔준다.

import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

b = [1]

for i in range(1, n):
    asc = 1
    for j in range(i-1, -1, -1):
        if a[i] > a[j] and asc < b[j] + 1:
            asc = b[j] + 1

    b.append(asc)
print(max(b))
