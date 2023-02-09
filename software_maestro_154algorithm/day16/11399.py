n = int(input())
a = list(map(int, input().split()))
a.sort()
result = a[0]
for i in range(1, n):
    a[i] += a[i - 1]
    result += a[i]

print(result)