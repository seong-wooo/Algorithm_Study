n, k = map(int, input().split())

if n < k * (k + 1) // 2:
    print(-1)

else:
    n -= k * (k + 1) // 2
    n %= k

    if n == 0:
        print(k - 1)

    else:
        print(k)
