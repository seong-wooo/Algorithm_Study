import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
a_nums = list(map(int, sys.stdin.readline().split()))

ten_num = 0
# a -> 10
for i in range(len(a_nums) - 1, -1, -1):
    a_nums[i] *= (a ** (len(a_nums) - 1 - i))

ten_num = sum(a_nums)

# 10 -> b
result = []
while ten_num:
    ten_num, r = ten_num // b, ten_num % b
    result.append(r)
print(" ".join(map(str, reversed(result))))
