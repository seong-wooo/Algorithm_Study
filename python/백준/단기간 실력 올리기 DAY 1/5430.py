# R 뒤집기 - 배열에 있는 수의 순서 뒤집음
# D 버리기 - 첫 번째 수 버림 - 배열 비어있을 시 에러

import sys
from collections import deque

front_or_back = 1
for _ in range(int(sys.stdin.readline())):
    ps = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())

    nums = deque(sys.stdin.readline().lstrip("[").rstrip("]\n").split(","))
    front_or_back = 1
    if ps.count("D") > n:
        print("error")
        continue

    for p in ps:
        if p == "R":
            front_or_back *= -1

        else:
            if front_or_back > 0:
                nums.popleft()
            else:
                nums.pop()

    if front_or_back < 0:
        nums.reverse()

    print("[" + ",".join(nums) + "]")
