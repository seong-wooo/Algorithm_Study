import sys

n = int(sys.stdin.readline())
lines = [0] * (1000001)

for _ in range(n):
    lines[int(sys.stdin.readline())] += 1


def find_num(start):
    while start >= 0 and lines[start] == 0:
        start -= 1

    return start


# a + b > c
start = 1000000
while True:
    big = find_num(start)
    if big < 0:
        print("-1")
        break

    if lines[big] >= 3:
        print(big * 3)
        break

    small1 = find_num(big - 1)
    if small1 < 0:
        print("-1")
        break

    if lines[big] == 2:
        print(big * 2 + small1)
        break

    # 큰 변 1개
    if lines[small1] >= 2:
        if small1 * 2 > big:
            print(big + small1 * 2)
            break
        start = small1
        continue

    # 큰 변 1개 작은 변 1개
    small2 = find_num(small1 - 1)
    if small2 < 0:
        print("-1")
        break

    if small1 + small2 > big:
        print(small1 + small2 + big)
        break

    start = small1

