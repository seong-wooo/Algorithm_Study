import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = [0, 0, 0]


def dfs(y, x, p_len):
    for j in range(y, y + p_len):
        for i in range(x, x + p_len):
            if paper[j][i] != paper[y][x]:
                p_len //= 3
                for k in range(3):
                    for l in range(3):
                        dfs(y + k * p_len, x + l * p_len, p_len)
                return
    result[paper[y][x]] += 1


dfs(0, 0, n)
print("\n".join(map(str, [result[-1], result[0], result[1]])))
