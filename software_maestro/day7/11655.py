s = input()
result = ""

for i in s:

    if i.islower():
        rot = ord(i) + 13
        result += chr(rot - 122 + 96) if rot > 122 else chr(rot)

    elif i.isupper():
        rot = ord(i) + 13
        result += chr(rot - 90 + 64) if rot > 90 else chr(rot)
    else:
        result += i

print(result)