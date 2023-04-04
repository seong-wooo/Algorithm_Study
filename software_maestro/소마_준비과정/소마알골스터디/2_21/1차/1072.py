import sys
from math import ceil
x, y = map(int, sys.stdin.readline().split())


def game(x, y):

    z = (y * 100 // x) + 1

    if z >= 100:
        return -1


    return ceil((z * x - 100 * y) / (100 - z))

print(game(x, y))
