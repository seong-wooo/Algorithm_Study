# 최대 7980

e, s, m = map(int, input().split())

a, b, c = 1, 1, 1

for i in range(1, 15 * 28 * 19 + 1):
    if (a, b, c) == (e, s, m):
        break
    a = a + 1 if a + 1 <= 15 else 1
    b = b + 1 if b + 1 <= 28 else 1
    c = c + 1 if c + 1 <= 19 else 1

print(i)