# 인덱스를 방문하면서 기름 값의 최소를 계속 갱신한다
# 최소의 기름 값 * 거리를 계속 더해준다.

import sys

# 도시의 개수
n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

total = 0
i = 0
min_cost = cost[0]
for i in range(n-1):
    min_cost = min(min_cost, cost[i])
    total += min_cost * distance[i]

print(total)