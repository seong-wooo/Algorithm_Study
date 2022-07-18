for t in range(int(input())):
    c, g = 0, 0
    for n in range(int(input())):
        C, G = map(float, input().split())
        c += C
        g += C * G

    print("%d %.1f" % (c, g/c))