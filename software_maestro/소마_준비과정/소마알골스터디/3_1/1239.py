import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()

if max(s) > 50:
    print("0")

else:
    result = 0
    for p in list(permutations(s, n)):
        line = []
        count = 0
        for i in p:
            count += i
            line.append(count)

        lines = 0
        for j in range(len(line) - 1):
            for k in range(j + 1, len(line)):
                if line[j] + 50 == line[k]:
                    lines += 1

        result = max(result, lines)

    print(result)