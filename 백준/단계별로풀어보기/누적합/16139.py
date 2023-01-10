import sys

s = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

alr = [sys.stdin.readline().split() for _ in range(q)]

mx = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    index = ord(s[i]) - 97

    for j in range(26):
        mx[j][i + 1] = mx[j][i]

    mx[index][i + 1] += 1

ans = []

for a, l, r in alr:
    index = ord(a) - 97
    ans.append(str(mx[index][int(r) + 1] - mx[index][int(l)]))

print("\n".join(ans))
