x = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        x.append(num)
if not x:
    print(-1)
else:
    print(sum(x))
    print(min(x))
