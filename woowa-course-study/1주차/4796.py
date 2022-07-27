# p일 중 l일동안 사용 가능

i = 1
while True:
    l, p, v = map(int, input().split())

    if l == p == v == 0:
        break

    result = v // p * l + min(v % p, l)

    print(f"Case {i}: {result}")
    i += 1
