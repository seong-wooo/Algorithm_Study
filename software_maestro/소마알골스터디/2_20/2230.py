import sys
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())

a = sorted(set(int(input()) for _ in range(n)))


left = 0
right = 0
answer = a[-1] - a[0]

while right < len(a):
    diff = a[right] - a[left]

    if diff == m:
        answer = m
        break

    elif diff > m:
        if answer > diff:
            answer = diff
        left += 1

    else:
        right += 1

print(answer)