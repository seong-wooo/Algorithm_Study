n = int(input())

a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse= True)


print(sum([a[i] * b[i] for i in range(n)]))

