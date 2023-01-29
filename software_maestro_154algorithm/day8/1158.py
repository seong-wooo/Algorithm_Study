n, k = map(int, input().split())

nums = [i for i in range(1, n + 1)]

result = []
index = 0

while nums:
    index = (index + k - 1) % len(nums)
    result.append(str(nums.pop(index)))

print("<" + ", ".join(result) + ">")
