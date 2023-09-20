# 수열의 규칙을 찾고 이를 코드로 구현한다.
# 찾은 수열의 규칙: p[n] = p[n-1] + p[n-5]

t = int(input())
p = [0, 1, 1, 1, 2]

for i in range(t):
    n =int(input())
    if len(p) > n:
        print(p[n])
    else:
        while len(p) < n+1:
            p.append(p[-1] + p[-5])
        print(p[-1])
