input()

a = list(map(int, input().split()))
minimum = a[0]
maximum = a[0]

for i in a:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i

print(minimum, maximum)
