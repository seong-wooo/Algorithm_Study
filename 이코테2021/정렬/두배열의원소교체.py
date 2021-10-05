# 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
  if a[i] < b[-1-i]:
    a[i] = b[-1-i]
  else:
    break

print(sum(a))