n, m = map(int, input().split())


def count_n(num, n):
    i = 0
    while n ** i <= num:
        i += 1

    result = 0
    for j in range(1, i):
        result += num // (n ** j)

    return result


count_five = count_n(n, 5) - count_n(m, 5) - count_n(n - m, 5)
count_two = count_n(n, 2) - count_n(m, 2) - count_n(n - m, 2)


print(min(count_five, count_two))
