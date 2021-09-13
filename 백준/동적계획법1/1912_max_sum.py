

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d =  [a[0]]
for i in range(1, n):
    d.append( max(d[i-1] + a[i], a[i]))

print(max(d))
