import sys

# A: 65
# H: 72
input = sys.stdin.readline


def R(k, r):
    if k[0] + 1 == r[0] and k[1] == r[1]:
        if r[0] < 72:
            r[0] += 1
            k[0] += 1

    else:
        if k[0] < 72:
            k[0] += 1

def L(k, r):
    if k[0] - 1 == r[0] and k[1] == r[1]:
        if r[0] > 65:
            r[0] -= 1
            k[0] -= 1
    else:
        if k[0] > 65:
            k[0] -= 1


def B(k, r):
    if k[0] == r[0] and k[1] - 1 == r[1]:
        if r[1] > 1:
            r[1] -= 1
            k[1] -= 1
    else:
        if k[1] > 1:
            k[1] -= 1


def T(k, r):
    if k[0] == r[0] and k[1] + 1 == r[1]:
        if r[1] < 8:
            r[1] += 1
            k[1] += 1
    else:
        if k[1] < 8:
            k[1] += 1


def RT(k, r):
    if k[0] + 1 == r[0] and k[1] + 1 == r[1]:
        if r[0] < 72 and r[1] < 8:
            r[0] += 1
            r[1] += 1
            k[0] += 1
            k[1] += 1

    else:
        if k[0] < 72 and k[1] < 8:
            k[0] += 1
            k[1] += 1

def LT(k, r):
    if k[0] - 1 == r[0] and k[1] + 1== r[1]:
        if r[0] > 65 and r[1] < 8:
            r[0] -= 1
            r[1] += 1
            k[0] -= 1
            k[1] += 1

    else:
        if k[0] > 65 and k[1] < 8:
            k[0] -= 1
            k[1] += 1

def RB(k, r):
    if k[0] + 1 == r[0] and k[1] - 1 == r[1]:
        if r[0] < 72 and r[1] > 1:
            r[0] += 1
            r[1] -= 1
            k[0] += 1
            k[1] -= 1
    else:
        if k[0] < 72 and k[1] > 1:
            k[0] += 1
            k[1] -= 1

def LB(k, r):
    if k[0] - 1 == r[0] and k[1] - 1 == r[1]:
        if r[0] > 65 and r[1] > 1:
            r[0] -= 1
            r[1] -= 1
            k[0] -= 1
            k[1] -= 1
    else:
        if k[0] > 65 and k[1] > 1:
            k[0] -= 1
            k[1] -= 1



k, r, n = input().split()

k = [ord(k[0]), int(k[1])]
r = [ord(r[0]), int(r[1])]


d = {
    "R": R,
    "L": L,
    "B": B,
    "T": T,
    "RT": RT,
    "LT": LT,
    "RB": RB,
    "LB": LB
}

for _ in range(int(n)):
    d[input().rstrip()](k, r)

print("".join([chr(k[0]), str(k[1])]))
print("".join([chr(r[0]), str(r[1])]))
