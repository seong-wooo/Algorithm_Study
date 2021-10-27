for _ in range(int(input())):
    s = 0
    for i in range(int(input())):
        u = input().split()
        a, b = u[0], int(u[1])
        if b > s:
            s = b
            university = a

    print(university)
