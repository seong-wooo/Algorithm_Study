from itertools import combinations

n = int(input())
r = []
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        r.append(int("".join(map(str,sorted(c, reverse=True)))))
r.sort()

if n >= len(r):
    print("-1")

else:
    print(r[n])
