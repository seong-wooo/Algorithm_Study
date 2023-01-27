import sys

a = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
a.sort()

for i in a:
    print(i)