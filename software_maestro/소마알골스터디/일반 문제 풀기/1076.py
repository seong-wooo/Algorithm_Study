d = {}

d["black"] = 0
d["brown"] = 1
d["red"] = 2
d["orange"] = 3
d["yellow"] = 4
d["green"] = 5
d["blue"] = 6
d["violet"] = 7
d["grey"] = 8
d["white"] = 9

colors = [input() for i in range(3)]

print(int(str(d[colors[0]]) + str(d[colors[1]])) * (10 ** d[colors[2]]))
