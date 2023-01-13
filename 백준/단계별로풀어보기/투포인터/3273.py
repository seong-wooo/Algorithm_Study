import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

x = int(sys.stdin.readline())

i = 0
j = n - 1
result = 0

while i < j:
    if nums[i] + nums[j] < x:
        i += 1

    elif nums[i] + nums[j] == x:
        result += 1
        i += 1
        j -= 1

    else:
        j -= 1

print(result)
