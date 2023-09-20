import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
friends = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1  # a에서 b로 한 다리
    friends[b][a] = 1  # b에서 a로 한 다리

for i in range(1, n + 1):
    friends[i][i] = 0

for k in range(1, n + 1):
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            friends[j][i] = min(friends[j][k] + friends[k][i], friends[j][i])

result = INF
ans = INF
for i in range(1, n + 1):
    k = sum(friends[i][1:])
    if k < result:
        result = k
        ans = i

print(ans)
