import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))