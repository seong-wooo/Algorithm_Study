import sys
from collections import Counter

a = Counter([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])

print(max(a, key=lambda x: (a[x], -x)))