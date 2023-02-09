n, m, k = map(int, input().split())

result = 0
for i in range(k + 1):
    result = max(result, min((n - i) // 2, m - k + i))

print(result)
