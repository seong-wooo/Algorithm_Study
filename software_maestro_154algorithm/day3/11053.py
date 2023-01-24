import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = [0]

for num in a:
    if num > stack[-1]:
        stack.append(num)
    else:
        index = bisect_left(stack, num)
        stack[index] = num

print(len(stack) - 1)