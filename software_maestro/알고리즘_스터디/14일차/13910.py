import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))

one_turn_dishes = set(s)
for a, b in combinations(s, 2):
    one_turn_dishes.add(a + b)

INF = 1e9
dishes = [INF] * (n + 1)

for x in one_turn_dishes:
    if x <= n:
        dishes[x] = 1


for x in range(1, n + 1):
    if dishes[x] == INF:
        for y in one_turn_dishes:
            if x - y > 0:
                dishes[x] = min(dishes[x], dishes[x - y] + 1)

print(dishes[-1] if dishes[-1] < INF else -1)