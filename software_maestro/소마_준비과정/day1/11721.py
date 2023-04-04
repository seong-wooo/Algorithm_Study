string = input()

i = 0
length = len(string)
while 10 * (i + 1) <= length:
    print(string[10 * i: 10 * (i + 1)])
    i += 1

print(string[10 * i:])
