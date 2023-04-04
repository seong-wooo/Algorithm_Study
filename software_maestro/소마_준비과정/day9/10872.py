result = 0
for i in range(5, int(input()) + 1, 5):
    while i % 5 == 0:
        result += 1
        i //= 5

print(result)