n = input()
length = len(n)

d = [1] * 2 + [0] * (length - 1)

if n[0] == "0":
    print("0")

else:
    if length < 2:
        print("1")
    else:
        invalid = {"00", "30", "40", "50", "60", "70", "80", "90"}

        for i in range(1, length):
            t = n[i - 1: i + 1]

            if t in invalid:
                break

            if t[0] == "0":
                d[i + 1] = d[i]

            elif t[1] == "0":
                d[i + 1] = d[i - 1]

            elif int(t) > 26:
                d[i + 1] = d[i]

            else:
                d[i + 1] = d[i - 1] + d[i]

        print(d[i + 1] % 1000000)


