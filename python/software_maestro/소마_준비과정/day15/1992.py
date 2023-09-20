import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())

video = [list(input().rstrip()) for _ in range(n)]


def press(video, y, x, length):
    result = ""
    for j in range(y, y + length):
        for i in range(x, x + length):
            if video[j][i] != video[y][x]:
                length //= 2
                result += "("
                for k in range(2):
                    for l in range(2):
                        result += press(video, y + length * k, x + length * l, length)
                result += ")"
                return result
    return video[y][x]


print(press(video, 0, 0, n))