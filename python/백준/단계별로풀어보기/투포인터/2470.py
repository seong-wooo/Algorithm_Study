import sys
from bisect import bisect_right

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

left = 0
right = n - 1

ans = [li[left], li[right]]
mix = abs(sum(ans))

while left < right:

    l = li[left]
    r = li[right]
    lr = l + r

    if abs(lr) < mix:
        ans = [l, r]
        mix = abs(lr)

    if lr < 0:
        left += 1
    else:
        right -= 1

print(*ans)