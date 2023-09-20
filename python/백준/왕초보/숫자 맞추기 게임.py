i = 1
while True:
    n = int(input())
    if n==0:
        break

    n1 = 3*n
    if n % 2 == 0:
        n2 = n1 / 2
    else:
        n2 = (n1+1) / 2
    n3 = 3 * n2

    n4 = n3 // 9

    if n1 % 2== 1:
        oe = "odd"
    else:
        oe = "even"

    print(f"{i}. {oe} {int(n4)}")
    i += 1