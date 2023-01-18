n = int(input())
f = int(input())

n_ = n - n % 100

n__f = n_ % f

if n__f == 0:
    print("00")
else:
    print(str(f - n__f).zfill(2))