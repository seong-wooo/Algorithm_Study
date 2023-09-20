# 처음에는 bfs를 이용할 뻔했다.
# 그냥 치킨집의 좌표, 집의 좌표를 따로 리스트에 모아둔다
# 조합을 이용하여 치킨집을 m의 크기를 갖는 부분집합으로 나눴다.
# 그리고 각 조합별로 집들과의 거리를 구하여 최솟값을 구한다.
# 처음에 distance 초기 설정을 [n] * len(house) 로 설정했다. 치킨 거리는 총 2*(n-1) 까지 나올 수 있다.
# 시간 776ms
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [input().split() for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1":
            house.append((i, j))
        elif graph[i][j] == "2":
            chicken.append((i, j))

chicken = list(combinations(chicken, m))

distance = sys.maxsize
for chicken_list in chicken:
    chicken_distance = [n * 2] * len(house)
    for c in chicken_list:
        for j in range(len(house)):
            chicken_distance[j] = min(chicken_distance[j], abs(c[0] - house[j][0]) + abs(c[1] - house[j][1]))

        distance = min(distance, sum(chicken_distance))

print(distance)







# 다풀고 수정해본 코드
# 시간 460ms
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [input().split() for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1":
            house.append((i, j))
        elif graph[i][j] == "2":
            chicken.append((i, j))

chicken = list(combinations(chicken, m))

distance = sys.maxsize
for chicken_list in chicken:
    # 새로운 리스트를 만드는 것이 아닌
    # 각 집합별로 치킨 최소 거리를 구해서 그 거리들 중 최솟값만 구한다.
    chicken_distance = 0
    for j in range(len(house)):
        chicken_distance += min([abs(c[0] - house[j][0]) + abs(c[1] - house[j][1]) for c in chicken_list])

    distance = min(distance, chicken_distance)

print(distance)