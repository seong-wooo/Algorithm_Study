import sys

input = sys.stdin.readline

n, c = map(int, input().split())

houses = sorted([int(input()) for _ in range(n)])

start = 0
end = houses[-1] - houses[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    total = 1
    for i in range(1, n):
        if houses[i] - current >= mid:
            current = houses[i]
            total += 1

    if total >= c:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)
