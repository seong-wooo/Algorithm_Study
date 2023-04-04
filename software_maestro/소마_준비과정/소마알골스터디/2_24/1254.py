s1 = input()
s2 = s1[::-1]
length = len(s1)
for i in range(length):
    if s1[i:] == s2[:length - i]:
        print(i + length)
        break
