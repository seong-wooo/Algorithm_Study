a, b, c = map(int, input().split())
d = int(input())

m = d//60
s = d%60

a = (a + (b + m + (c+s)//60) // 60) % 24
b = (b + m + (c+s)//60) % 60
c = (c + s) % 60
print(a,b,c)