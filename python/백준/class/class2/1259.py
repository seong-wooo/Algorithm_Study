import sys

while True:

    nums = sys.stdin.readline().rstrip()

    if nums == "0":
        break

    result = True
    for i in range(len(nums) // 2):
        if nums[i] != nums[-1 - i]:
            result = False
            break

    print("yes" if result else "no")