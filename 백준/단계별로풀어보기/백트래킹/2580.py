import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
a_zero = []

for j in range(9):
    for i in range(9):
        if a[j][i] == 0:
            a_zero.append((j, i))


def valid_num(i, j):
    valid_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행열 검사
    for k in range(9):
        if a[j][k] in valid_nums:
            valid_nums.remove(a[j][k])
        if a[k][i] in valid_nums:
            valid_nums.remove(a[k][i])

    j //= 3
    i //= 3
    for p in range(j * 3, (j + 1) * 3):
        for q in range(i * 3, (i + 1) * 3):
            if a[p][q] in valid_nums:
                valid_nums.remove(a[p][q])

    return valid_nums

def dfs(index):
    if index > len(a_zero) - 1:
        for a_ in a:
            print(*a_)
        exit(0)

    y, x = a_zero[index]

    valid_nums = valid_num(x, y)

    for nums in valid_nums:
        a[y][x] = nums
        dfs(index + 1)
        a[y][x] = 0

dfs(0)
