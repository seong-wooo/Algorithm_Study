import sys
from math import gcd

ans = []
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    ans.append(str(a * b // g))

print("\n".join(ans))