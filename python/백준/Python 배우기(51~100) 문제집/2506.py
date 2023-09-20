n = int(input())

result = list(map(int, input().split()))

total = [1 if result[0] == 1 else 0]
for i in range(1, n):
    if result[i] == 1:
        total.append(total[i-1] + 1)
    else:
        total.append(0)

print(sum(total))
