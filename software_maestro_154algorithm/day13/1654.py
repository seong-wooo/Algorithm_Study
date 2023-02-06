import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lines = [int(input()) for _ in range(k)]

start = 1
end = sum(lines) // n
ans = start
while start <= end:
    mid = (start + end) // 2

    if sum(i // mid for i in lines) >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)