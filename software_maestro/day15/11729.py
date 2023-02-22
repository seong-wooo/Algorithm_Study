import sys
sys.setrecursionlimit(10**6)
n = int(input())

result = []


def hanoi(n, start, end):
    if n == 1:
        result.append((start, end))

    else:
        hanoi(n - 1, start, 6 - start - end)
        hanoi(1, start, end)
        hanoi(n-1, 6 - start - end, end)


hanoi(n, 1, 3)

print(len(result))
for r in result:
    print(*r)