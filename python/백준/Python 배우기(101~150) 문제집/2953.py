result = []
for i in range(5):
    result.append(sum(map(int, input().split())))

m = max(result)
print(f"{result.index(m) + 1} {m}")