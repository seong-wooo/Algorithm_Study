import sys
from bisect import bisect_right


input = sys.stdin.readline
n, k = map(int, input().split())

a = [int(input()) for _ in range(n)]

result = 0
while k > 0:
    index = bisect_right(a, k) - 1
    result += k // a[index]
    k %= a[index]

print(result)