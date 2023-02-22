import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
trees = Counter((map(int, input().split())))

start = 0
end = int(1e9)
ans = 0
while start <= end:
    mid = (start + end) // 2

    total = sum((h - mid) * i for h, i in trees.items() if h > mid)
    if total > m:
        ans = mid
        start = mid + 1
    elif total == m:
        ans = mid
        break
    else:
        end = mid - 1

print(ans)
