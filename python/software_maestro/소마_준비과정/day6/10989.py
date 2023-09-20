import sys

a = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    a[int(sys.stdin.readline())] += 1

ans = ""

for i in range(1, 10_001):
    for j in range(a[i]):
        print(i)

print(ans)