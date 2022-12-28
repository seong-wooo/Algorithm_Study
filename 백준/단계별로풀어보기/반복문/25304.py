import sys

total = int(sys.stdin.readline())

result = 0

for i in range(int(sys.stdin.readline())):
    m = list(map(int, sys.stdin.readline().split()))
    result += m[0] * m[1]

if result != total:
    print("No")
else:
    print("Yes")


