from itertools import combinations
from math import factorial

n = int(input())

if n <= 10:
    print(n)

else:
    z = 2
    n -= 10
    while z < 10:
        count = factorial(10) // (factorial(10 - z) * factorial(z))
        if n >= count:
            n -= count
            z += 1

        else:
            break

    if z == 10 and n > 0:
        print("-1")
    else:
        print("".join(sorted(map(lambda x: sorted(x, reverse=True), combinations([str(i) for i in range(10)], z)))[n]))
