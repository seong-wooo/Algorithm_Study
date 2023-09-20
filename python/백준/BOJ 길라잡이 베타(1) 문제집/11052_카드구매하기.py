# 그냥 dp문제
n = int(input())
price = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    for j in range(1, i//2 + 1):
        price[i] = max(price[i], price[i-j] + price[j])

print(price[-1])