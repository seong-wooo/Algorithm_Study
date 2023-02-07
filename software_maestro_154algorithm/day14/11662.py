from math import sqrt

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())


def dist(t):
    mx = (1 - t) * ax + bx * t
    my = (1 - t) * ay + by * t
    gx = (1 - t) * cx + dx * t
    gy = (1 - t) * cy + dy * t

    return sqrt((mx - gx) ** 2 + (my - gy) ** 2)


left = 0
right = 1

while right - left > 1e-9:
    left2 = (2 * left + right) / 3
    left3 = (left + 2 * right) / 3

    if dist(left2) < dist(left3):
        right = left3
    else:
        left = left2

print("{:.10f}".format(dist(left)))
