import sys
input = sys.stdin.readline


def reverse(j, i):
    change[j][i:i+3] = map(lambda x: 1 - x, change[j][i:i+3])
    change[j + 1][i:i+3] = map(lambda x: 1- x, change[j + 1][i:i+3])
    change[j + 2][i:i+3] = map(lambda x: 1- x, change[j + 2][i:i+3])


def has_one():
    for j in range(n):
        for i in range(m):
            if change[j][i] == 1:
                return True
    return False

n, m = map(int,input().split())


before = [list(map(int, list(input().rstrip()))) for _ in range(n)]
after = [list(map(int, list(input().rstrip()))) for _ in range(n)]


change = [[0] * m for _ in range(n)]

for j in range(n):
    for i in range(m):
        if before[j][i] != after[j][i]:
            change[j][i] = 1

# if 뒤집어야하는 것 1 else 0
count = 0
for j in range(n - 2):
    for i in range(m - 2):
        if change[j][i] == 1:
            reverse(j, i)
            count += 1


if has_one():
    print("-1")
else:
    print(count)

