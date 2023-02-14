import sys

input = sys.stdin.readline
s = set()


for i in range(int(input())):
    a = input().rstrip().split()

    if len(a) == 1:
        if a[0] == "all":
            s = set(i for i in range(1, 21))

        else:
            s = set()
        continue
    
    c, x = a[0], a[1]

    if c == "add":
        s.add(x)

    elif c == "check":
        print("1" if x in s else "0")

    elif c == "remove":
        s.discard(x)

    elif c == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.add(x)