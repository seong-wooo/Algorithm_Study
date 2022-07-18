n = int(input())

total = 0
for x in range(1, n + 1):
    total += x * (x + 1) + x*(x+1)//2

print(total)
