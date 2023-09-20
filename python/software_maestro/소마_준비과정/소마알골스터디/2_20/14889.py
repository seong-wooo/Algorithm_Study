import sys
from itertools import combinations


def calc(team):
    team_stat = 0
    team = list(team)
    for j in range(len(team) - 1):
        for i in range(j + 1, len(team)):
            team_stat += stat[team[j]][team[i]]
            team_stat += stat[team[i]][team[j]]

    return team_stat

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

min_stat = int(1e9)

a = set(i for i in range(n))
for c in combinations([i for i in range(n)], n // 2):
    min_stat = min(min_stat, abs(calc(c) - calc(a - set(c))))

    if min_stat == 0:
        break

print(min_stat)