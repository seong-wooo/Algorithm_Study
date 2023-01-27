from collections import Counter
s = Counter(input())
c = [0] * 26

for s_ in s:
    c[ord(s_) - 97] = s[s_]

print(*c)