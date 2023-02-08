import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())


def star(n):
    if n == 3:
        return ["***", "* *", "***"]

    n3 = n // 3
    pre = star(n3)
    stars = []

    for ps in pre:
        stars.append(ps * 3)

    for ps in pre:
        stars.append(ps + " " * n3 + ps)

    stars += stars[:n3]

    return stars

print("\n".join(star(n)))
