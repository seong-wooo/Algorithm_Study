total = 0
for i in range(5):
    a = int(input())
    if a >= 40:
        total += a
    else:
        total += 40

print(total//5)
