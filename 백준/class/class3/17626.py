n = int(input())

s = {i**2 for i in range(1, int(n ** 0.5) + 1)}


def a(n):
    if (n ** 0.5).is_integer():
        return 1


    for t in s:
        if n - t in s:
            return 2

    for i in s:
        for j in s:
            if n - i - j in s:
                return 3

    return 4


print(a(n))

