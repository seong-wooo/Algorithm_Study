import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline


n = int(input())

set_u = set([int(input()) for _ in range(n)])
sum_uu = set(sum(c) for c in combinations_with_replacement(set_u, 2))

u = sorted(set_u)
def find_d():
    for i in range(n - 1, -1, -1):
        for su in sum_uu:
            if u[i] - su in set_u:
                return u[i]

print(find_d())