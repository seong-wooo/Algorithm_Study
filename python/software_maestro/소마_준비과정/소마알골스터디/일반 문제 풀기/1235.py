import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
nums = [input().rstrip() for _ in range(n)]

for k in range(1, 101):
    s = set()
    answer = True
    for i in range(n):
        if nums[i][-k:] in s:
            answer = False
            break
        s.add(nums[i][-k:])

    if answer:
       print(k)
       break
