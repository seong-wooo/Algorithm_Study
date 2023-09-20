import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()

result = deque(s[0])
for i in range(1, len(s)):
    if s[i] != result[-1]:
        result.append(s[i])

print(len(result) // 2)

# 풀이 2
# import sys
# import re
#
# input = sys.stdin.readline
#
# s = input().strip()
#
# print(len(re.findall("1+|0+", s)) // 2)


# 풀이 3
# print(max(s.count("01"), s.count("10")))
