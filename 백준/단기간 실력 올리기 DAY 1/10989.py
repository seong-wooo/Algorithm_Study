import sys

nums = [0] * 10001

for x in range(int(sys.stdin.readline())):
    nums[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for c in range(nums[i]):
        print(i)