a, b = map(int, input().split())
c = int(input())

a = (a+c//60 + (b + c%60) // 60) % 24
b = (b + c%60) % 60

print(a,b)