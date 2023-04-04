s = input()
index = [-1] * 26

for i in range(len(s)):
    od = ord(s[i]) - 97
    if index[od] == -1:
        index[od] = i

print(*index)

