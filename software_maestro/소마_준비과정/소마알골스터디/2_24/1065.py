from itertools import combinations

n = int(input())

if n < 100:
    print(n)

else:
    count = 99
    for num in range(111, n + 1):
        h = num // 100
        t = (num - h * 100) // 10
        o =  num % 10

        if h - t == t - o:
            count += 1

    print(count)