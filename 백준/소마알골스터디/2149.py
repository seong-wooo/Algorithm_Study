key = list(input())
plain = input()

order = sorted(enumerate(key), key=lambda x: (x[1], x[0]))
length = len(plain) // len(key)
plains = [plain[i:i+length] for i in range(0, len(plain), length)]

plains = list(zip(*plains))

result = ""
line = [""] * len(key)
for i in range(len(plains)):
    for j in range(len(order)):
        origin_index = order[j][0]
        line[origin_index] = plains[i][j]
    result += "".join(line)

print(result)
