import sys

result = sorted([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))],
                key=lambda x: (x[1], x[0]))

for xy in result:
    print(xy[0], xy[1])
