import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

c = [list(map(int, input().split())) for _ in range(n)]

maximum = 0
for x, y, z in combinations([i for i in range(m)], 3):

    result = 0
    for j in range(n):
        result += max(c[j][x], c[j][y], c[j][z])

    maximum = max(maximum, result)

print(maximum)