result = []

n, k = map(int, input().split())

x = [i for i in range(1, n + 1)]

index = 0
while x:
    index = (index + k - 1) % len(x)
    result.append(x.pop(index))


print("<" + ", ".join(map(str, result)) + ">")