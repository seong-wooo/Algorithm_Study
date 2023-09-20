import sys

n, c = map(int, sys.stdin.readline().split())

x = [int(sys.stdin.readline()) for _ in range(n)]

x.sort()

x_max = x[-1] - x[0]

start = 1
end = x[-1] - x[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cur = x[0]
    cnt = 1

    for i in range(1, n):
        if x[i] >= cur + mid:
            cur = x[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)