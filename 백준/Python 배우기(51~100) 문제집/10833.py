total = 0
for i in range(int(input())):
    s, a = map(int, input().split())
    total += a % s
print(total)