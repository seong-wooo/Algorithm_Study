peoples = [0]
for i in range(1, 5):
    x, y = map(int, input().split())
    peoples.append(peoples[i-1] - x + y)

print(max(peoples))
