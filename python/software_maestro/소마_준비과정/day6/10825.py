import sys

a = [tuple(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]

a.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print("\n".join(map(lambda x: x[0], a)))
