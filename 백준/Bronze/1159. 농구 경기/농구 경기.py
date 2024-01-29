import sys
from collections import Counter

input = sys.stdin.readline

names = Counter([input()[0] for _ in range(int(input()))])

answer = []
for name in names:
    if names[name] >= 5:
        answer.append(name)

print("".join(sorted(answer)) if answer else "PREDAJA")