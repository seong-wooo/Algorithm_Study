for i in range(int(input())):
    a,*b = input().split()
    a = float(a)
    for s in b:
        if s == "@":
            a *= 3
        elif s == "%":
            a += 5
        else:
            a -= 7
    print("%.2f"%a)