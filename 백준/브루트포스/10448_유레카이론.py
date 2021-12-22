def t_n(n):
    return n * (n + 1) // 2

import sys

input = sys.stdin.readline

num = [int(input()) for i in range(int(input()))]

tn = [t_n(i) for i in range(1, 46)]

triangle = [0] * 1001

for x in tn:
    for y in tn:
        for z in tn:
            if x + y + z <= 1000:
                triangle[x + y + z] = 1

for n in num:
    print(triangle[n])