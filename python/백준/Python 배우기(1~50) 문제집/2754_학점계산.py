s = input()
if s == "F":
    print(0.0)
else:
    g = 4.0 + 65 - ord(s[0])
    if s[1] == "+":
        g += 0.3
    elif s[1] =="-":
        g -= 0.3
    print(g)