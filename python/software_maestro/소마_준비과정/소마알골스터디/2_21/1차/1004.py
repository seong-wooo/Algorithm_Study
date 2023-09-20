import sys

input = sys.stdin.readline


def include(c_x, c_y, r, x, y):
    return ((c_x - x) ** 2 + (c_y - y) ** 2) ** 0.5 < r


for _ in range(int(input())):
    s_x, s_y, e_x, e_y = map(int, input().split())
    n = int(input())
    circles = [list(map(int, input().split())) for _ in range(n)]


    # s를 둘러싼 원의 개수 + e를 둘러싼 원의 개수 - 둘 다 속한 원의 개수

    result = 0
    for c in circles:
        a = include(c[0], c[1], c[2], s_x, s_y)
        b = include(c[0], c[1], c[2], e_x, e_y)

        if a is not b:
            result += 1

    print(result)

