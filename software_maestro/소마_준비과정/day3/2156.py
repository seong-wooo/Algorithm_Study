import sys

n = int(sys.stdin.readline())
grapes = [int(sys.stdin.readline()) for _ in range(n)]

drinks = [[0] * n for i in range(2)]
drinks[0][0] = grapes[0]

if n > 1:
    # 전꺼 마시기
    # 전전꺼 마시기
    drinks[0][1] = grapes[0] + grapes[1]
    drinks[1][1] = grapes[1]

    for i in range(2, n):
        drinks[0][i] = max(drinks[1][i - 1] + grapes[i], drinks[0][i - 1])
        drinks[1][i] = max(drinks[0][i- 2], drinks[1][i - 2]) + grapes[i]

print(max(drinks[0][-1], drinks[1][-1]))
