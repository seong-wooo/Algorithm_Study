import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
sangg = Counter(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
for i in range(m):
    find[i] = str(sangg[find[i]]) if find[i] in sangg else "0"

print(" ".join(find))
