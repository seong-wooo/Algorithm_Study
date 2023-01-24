import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    stickers = [list(map(int, sys.stdin.readline().split())) for j in range(2)]

    length = len(stickers[0])
    if length > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

        for l in range(2, length):
            stickers[0][l] += max(stickers[1][l - 1], stickers[0][l - 2], stickers[1][l - 2])
            stickers[1][l] += max(stickers[0][l - 1], stickers[0][l - 2], stickers[1][l - 2])

    print(max(stickers[0][-1], stickers[1][-1]))