import sys

ans = []
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    if s == s[::-1]:
        ans.append(f'1 {len(s) // 2 + 1}')
        continue
    for i in range((len(s) + 1) // 2):
        if s[i] != s[-1 - i]:
            ans.append(f'0 {i + 1}')
            break

print("\n".join(ans))

