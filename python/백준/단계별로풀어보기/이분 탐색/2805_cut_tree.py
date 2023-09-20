# 잘라야하는 나무의 길이를 기준으로 이분 탐색을 진행하였다.
# 잘린 나무의 길이를 구하는 과정에서 시간초과가 났다.
# 리스트 만들 때 i-mid if i > mid else 0 for i in tree 이런식으로 사용하는 것을 배웠다

import sys

n, m  = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

high = max(tree)
low = 1

while low <= high:
    mid = (high + low ) //2
    cut = sum(i-mid if i > mid else 0 for i in tree)

    if cut >= m:
        low = mid + 1

    else:
        high = mid - 1


print(high)





