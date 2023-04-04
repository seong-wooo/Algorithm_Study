import sys
import math

input = sys.stdin.readline

while True:
    a = input().rstrip()

    if not a:
        break

    n, m = map(int, a.split())

    INF = int(1e9)
    min_all, min_one = INF, INF

    for _ in range(m):
        al, on = map(int, input().split())
        min_all, min_one = min(min_all, al), min(min_one, on)

    print(min(min_all * math.ceil(n/6), min_all * (n//6) + min_one * (n % 6), n * min_one))