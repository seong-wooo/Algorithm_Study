# L <= 문제 난이도 합 <= R
# 제일 큰 난이도 - 제일 작은 난이도 >= X
import sys
from itertools import combinations

input = sys.stdin.readline

n, l, r, x = map(int, input().split())

a = list(map(int, input().split()))

answer = 0
for i in range(2, n + 1):
    for combi in combinations(a, i):
        combi = sorted(combi)

        if combi[-1] - combi[0] >= x and l <= sum(combi) <= r:
            answer += 1

print(answer)