import sys

max_num = 1000000
nums = [False] * 2 + [True] * (max_num - 1)

for i in range(2, int(max_num ** 0.5) + 1):
    if nums[i]:
        nums[i * 2::i] = [False] * ((max_num - i) // i)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3, n // 2 + 1, 2):
        if nums[i] and nums[n - i]:
            print(f"{n} = {i} + {n - i}")
            break

