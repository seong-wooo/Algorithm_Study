n = int(input())
a = list(map(int, input().split()))

p = [0] * n

i = 0
for num in sorted(enumerate(a), key=lambda x: (x[1], x[0])):
    p[num[0]] = i
    i += 1


print(*p)