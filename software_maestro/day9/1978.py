import sys

n = int(sys.stdin.readline())
nums = [0] * 2 + [1 for _ in range(999)]
s = list(map(int, sys.stdin.readline().split()))

for x in range(2, 1001):
    for y in range(2 * x, 1001, x):
        if nums[y]:
            nums[y] = 0

print(sum(nums[x] for x in s))
