import sys
input =sys.stdin.readline
n = int(input())

a = [int(input()) for _ in range(n)]

if n == 1:
    print("0")
else:

    d = a[0]
    other = a[1:]
    count = 0
    while d <= max(other):
        i = other.index(max(other))
        d, other[i] = d + 1, other[i] - 1
        count += 1

    print(count)

