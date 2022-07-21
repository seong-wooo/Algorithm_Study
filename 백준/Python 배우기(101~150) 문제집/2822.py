result = []

for i in range(8):
    result.append(int(input()))

total = list(sorted(enumerate(result), key=lambda z: -z[1])[:5])

print(sum([x[1] for x in total]))
for y in sorted(total, key=lambda z: z[0]):
    print(y[0] + 1, end=" ")
