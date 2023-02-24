n, r, c = map(int, input().split())


def z(l, y, x):
    if l == 1:
        return 0

    l //= 2

    if y < l and x < l:
        return z(l, y, x)

    if y < l and x >= l:
        return l * l + z(l, y, x - l)

    if y >= l and x < l:
        return 2 * l * l + z(l, y - l, x)

    return 3 * l * l + z(l, y - l, x - l)


print(z(2**n, r, c))