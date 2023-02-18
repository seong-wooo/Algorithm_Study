import math
x, y = map(int, input().split())

target = (y * 100) // x + 1

if x == y or target == 100:
    print(-1)

else:
    print(math.ceil((target*x - 100*y)/(100 - target)))

