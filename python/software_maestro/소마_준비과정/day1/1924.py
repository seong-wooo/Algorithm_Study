x, y = map(int, input().split())

day = ["MON", "TUE", "WEN", "THU", "FRI", "SAT", "SUN"]

days = 0

thirty_one = {1, 3, 5, 7, 8, 10, 12}
thirty = {4, 6, 9, 11}

for i in range(1, x):
    if i in thirty_one:
        days += 31
    elif i in thirty:
        days += 30
    else:
        days += 28

days += y - 1

print(day[days % 7])

