b = 0
c = 1

for i in range(int(input()) - 1):
    b, c = c, b+ c

print(c)