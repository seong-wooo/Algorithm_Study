m, n = map(int, input().split())

nums = [False] * 2 + [True] * (n - 1)

for i in range(2, n + 1):
    if nums[i]:
        nums[2 * i::i] = [False] * ((n - i) // i)

for x in range(m, n + 1):
    if nums[x]:
        print(x)
