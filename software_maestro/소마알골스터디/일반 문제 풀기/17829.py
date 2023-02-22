import sys


def find_second(x, y):
    nums = []
    for j in range(y, y + 2):
        for i in range(x, x + 2):
            nums.append(p[j][i])

    return sorted(nums)[2]


def pooling(y, x, length):
    if length == 2:
        return find_second(y, x)

    length //= 2
    a = pooling(y, x, length)
    b = pooling(y + length, x, length)
    c = pooling(y, x + length, length)
    d = pooling(y + length, x + length, length)
    return sorted([a, b, c, d])[2]


input = sys.stdin.readline

n = int(input())

p = [list(map(int, input().split())) for _ in range(n)]

print(pooling(0, 0, n))
