import sys

a = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

a.sort(key=lambda x: (x[0], x[1]))

print("\n".join(map(lambda x: str(x[0]) + " " + str(x[1]), a)))