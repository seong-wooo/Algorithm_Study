import sys

input = sys.stdin.readline

n, k = map(int, input().split())
course = list(map(int, input().split()))

half_course = sum(course)

# 돌아오는 경우
if k // half_course == 1:
    k %= half_course

    i = n - 1
    while course[i] <= k:
        k -= course[i]
        i -= 1

# 출발지에서 출발하는 경우
else:
    k %= half_course

    i = 0
    while k >= course[i]:
        k -= course[i]
        i += 1

print(i + 1)