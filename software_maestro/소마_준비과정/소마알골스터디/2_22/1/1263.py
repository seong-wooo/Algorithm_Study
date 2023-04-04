import sys

input = sys.stdin.readline
n = int(input())

ts = [list(map(int, input().split())) for i in range(n)]

ts.sort(key=lambda x: x[1])


def valid_start(start):
    for t, s in ts:
        if start + t > s:
            return False
        start += t
    return True

def can_work():
    start = ts[0][1] - ts[0][0]
    for i in range(start, -1, -1):
        if valid_start(i):
            print(i)
            return True
    return False


if not can_work():
    print("-1")


# 4
# 3 5
# 10 14
# 5 20
# 1 16