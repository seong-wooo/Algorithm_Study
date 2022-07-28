import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
xy = set(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))

result = 0

for _ in range(len(xy)):
    x, y = xy.pop()
    if (x - a, y - b) in xy and (x - a, y) in xy and (x, y - b) in xy:
        result += 1

    if (x - a, y) in xy and (x - a, y + b) in xy and (x, y + b) in xy:
        result += 1

    if (x + a, y) in xy and (x, y + b) in xy and (x + a, y + b) in xy:
        result += 1

    if (x + a, y) in xy and (x, y - b) in xy and (x + a, y - b) in xy:
        result += 1

print(result)
