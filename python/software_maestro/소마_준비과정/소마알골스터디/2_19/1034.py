import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lamps = [list(input().rstrip()) for _ in range(n)]

k = int(input())

# 각 열 별로 1인 그룹과 0인 그룹을 나눈다.
# 키고 끌때마다 1인 그룹과 0인 그룹을 바꾼다.
#
light_group = [[[], []] for _ in range(m)]


for j in range(n):
    for i in range(m):
        if lamps[j][i] == "0":
            light_group[i][0].append(j)
        else:
            light_group[i][1].append(j)


def turn_on(i):
    light_group[i][0], light_group[i][1] = light_group[i][1], light_group[i][0]


