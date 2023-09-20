result = []

for i in range(46):
    for j in range(i):
        result.append(i)

a, b= map(int, input().split())

print(sum(result[a-1:b]))