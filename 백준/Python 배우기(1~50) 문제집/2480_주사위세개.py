x = list(map(int,input().split()))
if sum(x) / 3 == x[0]:
    print(10000+x[0] * 1000)
elif x[0]==x[1] or x[0] == x[2]:
    print(1000 + x[0] * 100)
elif x[1] == x[2]:
    print(1000 + x[1] * 100)
else:
    print(max(x) * 100)

