import sys

paper = [[0] * 100 for _ in range(100)]

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            paper[y + i][x + j] = 1

print(sum(sum(paper, [])))