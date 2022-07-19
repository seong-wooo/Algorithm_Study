total = 0
result = []
for x in range(10):
    o, i = map(int, input().split())
    total += i - o
    result.append(total)

print(max(result))