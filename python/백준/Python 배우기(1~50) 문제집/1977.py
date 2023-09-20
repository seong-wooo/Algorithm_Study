m, n = int(input()), int(input())

result = [i * i for i in range(1, 101) if m <= i*i <= n]
print(f"{sum(result)}\n{result[0]}" if result else "-1")
