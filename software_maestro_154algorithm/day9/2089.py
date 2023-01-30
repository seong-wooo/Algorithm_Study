n = int(input())

result = []

while n != 0:
    n, r = n // -2, n % -2

    if r == -1:
        n += 1
        r = 1
    result.append(r)

print("".join(map(str, reversed(result))) if result else 0)
