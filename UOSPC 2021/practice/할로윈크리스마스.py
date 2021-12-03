def changeNum(radix, n):
    n = n[::-1]
    return sum(int(n[i]) * (radix**i) for i in range(len(n)))


s, t = input().split()

radix_s = max(int(s[i]) for i in range(len(s))) + 1
radix_t = max(int(t[i]) for i in range(len(t))) + 1

count = 0
for i in range(radix_s, 11):
    for j in range(radix_t, 11):
        if changeNum(i, s) == changeNum(j, t):
            count += 1
print(count)