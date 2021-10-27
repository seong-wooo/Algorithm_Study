s = int(input())
if s <= 2:
    print(1)
else:
    for i in range(1, s+1):
        if i*(i+1)/2 > s:
            print(i-1)
            break