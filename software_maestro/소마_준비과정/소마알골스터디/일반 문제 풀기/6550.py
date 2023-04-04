import sys


def sol(s, t):
    index = 0
    for i in range(len(t)):
        if t[i] == s[index]:
            index += 1
            if index == len(s):
                return "Yes"
    return "No"

while True:
    inp = sys.stdin.readline().strip()
    if not inp:
        break

    strings, t = inp.split()

    print(sol(strings, t))