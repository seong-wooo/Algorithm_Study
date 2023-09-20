import sys

n = int(sys.stdin.readline())
paper = [sys.stdin.readline().split() for _ in range(n)]


def cut(n, y, x):
    if n == 1:
        return paper[y][x]

    result = ""
    p = paper[y][x]
    for j in range(y, y + n):
        for i in range(x, x + n):
            if paper[j][i] != p:
                n //= 2
                for l in range(2):
                    for k in range(2):
                        result += cut(n, y + l * n, x + k * n)
                return result

    return p

result = cut(n, 0, 0)
print(result.count("0"))
print(result.count("1"))
