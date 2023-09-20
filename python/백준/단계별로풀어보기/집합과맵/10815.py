import sys

ans = []

n = sys.stdin.readline()
dict = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    if i in dict:
        ans.append("1")
    else:
        ans.append("0")

print(" ".join(ans))