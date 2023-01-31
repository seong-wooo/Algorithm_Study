a, b = map(int, input().split())

def next(n, b):
    result = 0
    for i in str(n):
        result += int(i) ** b
    return result

s = []
while a not in s:
    s.append(a)
    a = next(a, b)

print(s.index(a))

