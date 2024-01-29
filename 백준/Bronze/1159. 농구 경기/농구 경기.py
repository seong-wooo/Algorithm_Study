import sys
from collections import Counter

input = sys.stdin.readline
names = Counter([input()[0] for _ in range(int(input()))])
answer = [name for name in names if names[name] >= 5]
print("".join(sorted(answer)) if answer else "PREDAJA")
