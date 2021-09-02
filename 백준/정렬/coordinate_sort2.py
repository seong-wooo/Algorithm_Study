# y좌표가 증가하는 순서
# y좌표가 같으면 x좌표가 증가하는 순서
# lambda 식을 이용하여 쉽게 정렬
# coordinate_sort 와 거의 같은 문제

import sys

n = int(sys.stdin.readline())

co = []
for i in range(n):
    co.append(list(map(int, sys.stdin.readline().split())))

co.sort(key=lambda x:(x[1], x[0]))

for j in co:
    print(j[0], j[1])