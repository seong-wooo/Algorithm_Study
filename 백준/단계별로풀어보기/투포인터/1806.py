import sys

n, s = map(int, sys.stdin.readline().split())

a = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    a[i] += a[i - 1]

if a[-1] < s:
    print("0")

else:
    ans = []

    i = 1
    j = 1
    while i < n + 1 and j < n + 1:
        if a[j] - a[i - 1] >= s:
            ans.append(j - i + 1)
            i += 1

        else:
            j += 1
    print(min(ans))
