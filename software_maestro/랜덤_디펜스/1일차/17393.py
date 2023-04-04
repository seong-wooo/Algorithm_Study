import sys
import bisect

input = sys.stdin.readline

# 각 타일 Ai Bi 가지고 있다
# i번째 타일 -> i번째 타일의 잉크지수보다 작거나 같은 점도지수를 가지는 칸을 칠할 수 있다.
# 각 칸의 잉크지수는 점도지수보다 크거나 같다
# 점도지수는 항상 오름차순 -> 이분 탐색을 사용한다.

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * n

for i in range(n - 1):
    index = bisect.bisect_right(b, a[i])
    if index > i + 1:
        result[i] = index - i - 1

print(" ".join(map(str,result)))


# 문제 해설
# 코딩 테스트에서 이진 탐색 문제가 나온다?
# 1. upper_bound , lower_bound 쓰는 문제: 카카오 2번 출제 된 적 있음
# upper_bound: bisect_right
# lower_bound: bisect_left

# 2. 파라메트릭 서치