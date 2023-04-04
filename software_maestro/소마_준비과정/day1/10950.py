import sys

ans = []

for i in range(int(sys.stdin.readline())):
   ans.append(sum(map(int, sys.stdin.readline().split())))

print("\n".join(map(str, ans)))