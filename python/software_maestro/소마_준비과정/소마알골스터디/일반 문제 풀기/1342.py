import sys
from collections import Counter


def dfs(pre, c):
    if len(s) == c:
        return 1

    count = 0
    for k in counter.keys():
        if  pre == k or counter[k] == 0:
            continue

        counter[k] -= 1
        count += dfs(k, c + 1)
        counter[k] += 1

    return count



s = input()
counter = Counter(s)

print(dfs("", 0))
