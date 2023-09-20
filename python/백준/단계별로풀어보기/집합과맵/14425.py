import sys

n, m = map(int, sys.stdin.readline().split())

s = set()

for _ in range(n):
    s.add(sys.stdin.readline())

result = 0

for _ in range(m):
    result = result + 1 if sys.stdin.readline() in s else result

print(result)

