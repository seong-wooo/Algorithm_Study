import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for j in range(n):
        for i in range(n):
            if not graph[j][i]:
                graph[j][i] = graph[j][k] & graph[k][i]

for g in graph:
    print(*g)
