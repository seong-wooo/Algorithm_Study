import sys
import math
input =sys.stdin.readline

n, m = map(int, input().split())

all_min = sys.maxsize
one_min = sys.maxsize

for _ in range(m):
    a, b = map(int, input().split())
    all_min = min(all_min, a)
    one_min = min(one_min, b)

print(min(all_min * math.ceil(n/6), all_min * (n//6) + one_min * (n % 6), one_min * n))

