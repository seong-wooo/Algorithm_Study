import sys

input = sys.stdin.readline

n = int(input())
all = set(map(int, input().split()))
m = int(input())
sangg = list(map(int, input().split()))

sangg_result = ["0"] * m

for i in range(m):
    if sangg[i] in all:
        sangg_result[i] = "1"

print(" ".join(sangg_result))

