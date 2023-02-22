n, l = map(int, input().split())

start = -1
length = 0
for i in range(l, 101):
    find_x = n / i - (i - 1) / 2
    if find_x.is_integer() and find_x >= 0:
        start = int(find_x)
        length = i
        break

if start != -1:
    print(*[start + j for j in range(length)])
else:
    print("-1")

