import sys
from itertools import combinations

# i번째 인사하면 체력 -= L[i], 기쁨 += j[i]
# 체력이 최소한으로 남을때까지 인사 -> 근데 기쁨 최대치여야함

input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

lj = [(L[i], J[i]) for i in range(n)]

result = 0
for i in range(1, n + 1):
   for c in combinations(lj, i):
        if sum(x[0] for x in c) < 100:
            result = max(result, sum(x[1] for x in c))

print(result)

# n <= 20이니까 완전 탐색을 고려한다
# 인사를 하는 경우, 안하는 경우
