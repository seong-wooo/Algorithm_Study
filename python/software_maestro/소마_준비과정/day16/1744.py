import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(a[0])

else:
    a.sort()
    mid = bisect_left(a, 0) # mid -1 까지 음수 mid ~ 끝까지  0 이상의 양수

    # 음수 작은것부터 곱하기 처리
    i = 0
    result = 0
    while i + 1 < mid:
        result += a[i] * a[i + 1]
        i += 2

    # i는 mid - 1 이거나 mid
    # mid가 짝수였다면, 음수끼리는 서로 곱할 수 있었음, 그렇다면 i = mid
    if mid % 2 == 1:
        if a[mid] == 0:
            i = mid + 1
        else:
            result += a[mid - 1]
            i = mid

    if not i and not a[i]:
        i += 1

    # 현재 i는 양수 중 제일 작은 값을 가리키고 있음
    if (n - i) % 2 == 1: # 홀수 개
        result += a[i]
        i += 1

    while i + 1 < n:
        result += max(a[i] * a[i + 1], a[i] + a[i+1])
        i += 2

    print(result)