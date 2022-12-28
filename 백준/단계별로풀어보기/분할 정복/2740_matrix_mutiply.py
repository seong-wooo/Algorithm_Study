# 행렬에 대해 알고 있다면 3중 루프로 바로 해결 가능했던 문제
# 항상 행과 열을 헷갈리지말자


import sys

n, m = map(int, sys.stdin.readline().split())


a = []
b = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())

for j in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

c =[[0 for _ in range(k)] for _ in range(n)]


for x in range(n):
    for y in range(k):
        for z in range(m):
            c[x][y] += a[x][z] * b[z][y]

for w in c:
    print(" ".join(map(str, w)))