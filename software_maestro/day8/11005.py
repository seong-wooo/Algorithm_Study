n, b = map(int, input().split())


def change(num):
    if num < 10:
        return str(num)
    return str(chr(num + 55))


result = ""

while n >= b:
    n, r = n // b, n % b
    result += str(change(r))
result += str(change(n))
print(result[::-1])

