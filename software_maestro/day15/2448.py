import sys
sys.setrecursionlimit(10**6)

n = int(input())

def a(n):
    if n == 3:
        return ["  *  ", " * * ", '*****']

    n //= 2
    x = a(n)
    c = [" " * n + i + " " * n for i in x]
    d = [i + " " + i for i in x]
    return  c + d

print("\n".join(a(n)))

