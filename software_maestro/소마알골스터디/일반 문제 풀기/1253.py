import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

nums = sorted((map(int, input().split())))

count = 0
for i in range(n):
    left = 0
    right = n - 1

    while left < right:
        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue

        h = nums[left] + nums[right]

        if h > nums[i]:
            right -= 1

        elif h < nums[i]:
            left += 1

        else:
            count +=1
            break
print(count)