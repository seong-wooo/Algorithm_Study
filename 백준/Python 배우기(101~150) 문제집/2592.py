nums = [int(input()) for i in range(10)]
print(sum(nums) // len(nums))
print(max(nums, key= nums.count))

