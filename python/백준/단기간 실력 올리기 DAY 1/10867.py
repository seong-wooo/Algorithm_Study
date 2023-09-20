input()

results = sorted(list(set(map(int, input().split()))))

for result in results:
    print(result, end=" ")
