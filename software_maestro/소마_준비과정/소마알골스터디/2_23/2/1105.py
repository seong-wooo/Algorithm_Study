l, r = map(int, input().split())
s_l = str(l)
s_r = str(r)

if len(s_l) < len(s_r):
    print("0")
else:
    result = 0
    i = 0
    while i < len(s_l) and s_l[i] == s_r[i]:
        i += 1

    print(s_l[:i].count("8"))
