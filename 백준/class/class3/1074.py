n, r, c = map(int, input().split())


def visit(n, y, x):
    if n == 0:
        return 0

    # y, x 가 몇 사분면인지?

    n2 = n // 2

    if y < n2 and x < n2:
        return visit(n2, y, x)

    if y < n2 and x >= n2:
        return n2*n2 + visit(n2, y, x - n2)

    if y >= n2 and x < n2:
        return 2*n2*n2 + visit(n2, y - n2, x)

    return n2*n2*3 + visit(n2, y - n2, x - n2)


print(visit(2**n, r, c))