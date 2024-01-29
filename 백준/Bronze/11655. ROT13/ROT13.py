s = input()
# A = 65
# Z = 90
# a = 97
# z = 122
result = ""

for i in range(len(s)):
    if s[i].islower():
        rot13 = ord(s[i]) + 13
        result += chr(rot13) if rot13 <= 122 else chr(rot13 - 122 + 96)

    elif s[i].isupper():
        rot13 = ord(s[i]) + 13
        result += chr(rot13) if rot13 <= 90 else chr(rot13 - 90 + 64)

    else:
        result += s[i]
print(result)
