n = int(input())
for i in range(n, 0, -1):
    stars = "*" * i
    print(stars.rjust(n, " "))