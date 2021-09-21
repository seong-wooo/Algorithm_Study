# 1. 증가하는 부분수열을 구한다
# 2. 역으로 증가하는 부분수열을 구한다.
# 3. 두 리스트의 같은 인덱스끼리 합해서 가장 큰 값을 구한다.
# 4. 1을 빼준다.


import sys


n = int(sys.stdin.readline())

s = list(map(int, sys.stdin.readline().split()))

asc=[1]
desc = [0 for _ in range(n)]
desc[-1] = 1

# 증가하는 부분수열
for i in range(1, n):
    ascend = 1
    for j in range(i-1, -1,-1):
        if s[i] > s[j] and ascend < asc[j] + 1:
            ascend = asc[j] + 1
    asc.append(ascend)

# 역으로 증가하는 부분수열
for i in range(n-2,-1,-1):
    ascend = 1
    for j in range(i+1,n):
        if s[i] > s[j] and ascend < desc[j] + 1:
            ascend = desc[j] + 1
    desc[i] += ascend


max_bitonic = 0
for i in range(n):
    max_bitonic = max(max_bitonic, asc[i] + desc[i])

print(max_bitonic - 1)
