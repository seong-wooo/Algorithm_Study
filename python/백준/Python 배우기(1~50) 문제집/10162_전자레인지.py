t = int(input())

m = t // 60
s = t % 60

if s % 10 != 0:
    print(-1)
else:
    a = m // 5
    b = m % 5

    print(a, b, s//10)