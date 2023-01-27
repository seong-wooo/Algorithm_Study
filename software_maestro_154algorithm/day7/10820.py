import sys

a_l = {chr(i) for i in range(97, 124)}
a_u = {chr(i) for i in range(65, 92)}

while True:
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        break

    l = 0
    u = 0
    d = 0
    b = 0
    for c in line:
        if c in a_l:
            l += 1
        elif c in a_u:
            u += 1
        elif c.isdigit():
            d += 1
        else:
            b += 1

    print(l, u, d, b)
