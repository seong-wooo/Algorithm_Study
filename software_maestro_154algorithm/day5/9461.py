import sys

p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    p_length = len(p)
    if n > p_length:
        for i in range(p_length, n):
            p.append(p[i - 1] + p[i - 5])
        print(p[n - 1])
    else:
        print(p[n - 1])
