import sys
import re

input = sys.stdin.readline
p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    signal = input().rstrip()
    if p.fullmatch(signal):
        print("YES")
    else:
        print("NO")