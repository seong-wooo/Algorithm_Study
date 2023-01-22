import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

li = [0]

for num in nums:
    if num > li[-1]:
        li.append(num)

    else:
        li[bisect_left(li, num)] = num

print(len(li) - 1)
