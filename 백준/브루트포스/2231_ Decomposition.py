# 분해합: abc = abc +a +b + c
# 숫자 하나하나마다 분해합을 구하여
# n과 같은지 확인한다

n = int(input())
constructor = False
for i in range(n):
    j = list(str(i))
    result = n - i
    for k in range(len(j)):
        result -= int(j[k])

    if result == 0:
        print(i)
        constructor = True
        break
    if constructor:
        break

if constructor == False:
    print(0)

# 소요 시간 줄이기 위한 수정 코드
# list(map(int, str(i) 를 이용해 각 자릿수를 나누는 것을 알게됨
# 최초의 constructor 0 으로 설정하여 중복된 코드를 방지한다


# n = int(input())
# constructor = 0
# for i in range(n):
#     j = list(map(int, str(i)))
#     if n == i + sum(j):
#         constructor = i
#         break
# print(constructor)


