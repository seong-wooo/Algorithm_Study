max_m = []
for i in range(int(input())):
    x = sorted((map(int, input().split())))

    if sum(x) / 3 == x[0]:
        m = 10000 + x[0] * 1000
    elif x[0] == x[1] or x[0] == x[2]:
        m = 1000 + x[0] * 100
    elif x[1] == x[2]:
        m = 1000 + x[1] * 100
    else:
        m = max(x) * 100
    max_m.append(m)


print(max(max_m))