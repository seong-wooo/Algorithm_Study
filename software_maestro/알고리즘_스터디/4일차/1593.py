import sys
from collections import Counter

input = sys.stdin.readline

len_w, len_s = map(int, input().split())
w = input().strip()
s = input().strip()
counter_w = [0] * 58
counter_s = [0] * 58

for i in w:
    counter_w[ord(i) -65] += 1

for i in range(len_w - 1):
    counter_s[ord(s[i]) - 65] += 1

left, right = 0, len_w - 1
result = 0
while right < len_s:
    counter_s[ord(s[right]) - 65] += 1

    if counter_w == counter_s:
        result += 1

    counter_s[ord(s[left]) - 65] -= 1
    left += 1
    right += 1

print(result)