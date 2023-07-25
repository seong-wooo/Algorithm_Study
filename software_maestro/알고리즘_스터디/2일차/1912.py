import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(nums[0])

else:
    dp = [nums[0]] + [0] * (n - 1) if nums[0] > 0 else [0] * n

    for i in range(1, n):
        result = dp[i - 1] + nums[i]
        if result > 0:
            dp[i] = result

    maximum = max(dp)

    print(maximum if maximum > 0 else max(nums))

