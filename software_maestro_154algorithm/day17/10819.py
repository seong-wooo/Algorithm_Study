import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

maximum = 0
for s in permutations(map(int, input().split()), n):

    result = 0
    for i in range(len(s)- 1):
        result += abs(s[i] - s[i+1])

    maximum = max(maximum, result)

print(maximum)
