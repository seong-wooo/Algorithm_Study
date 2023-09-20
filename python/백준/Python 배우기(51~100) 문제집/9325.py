import sys

for i in range(int(sys.stdin.readline())):
    s = int(sys.stdin.readline())
    for j in range(int(sys.stdin.readline())):
        q, p = map(int, sys.stdin.readline().split())
        s += q * p
    print(s)