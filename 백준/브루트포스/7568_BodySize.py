# 자기보다 큰 사람이 몇명인지 등수 세기
# 자기보다 큰 사람이 몇명인지만 알면 된다
# 다른거는 필요없다

def bigger(n ,m):
    if n[0] < m[0] and n[1] < m[1]:
        return True
    return False

n = int(input())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if bigger(a[i], a[j]):
            rank+=1
    b.append(rank)
print(" ".join(map(str, b)))


# 불필요한 코드 수정
# 살짝 줄였음
# b 리스트 하나 없애고 출력을 바로 진행한다.


# def bigger(n ,m):
#     if n[0] < m[0] and n[1] < m[1]:
#         return True
#     return False
#
# n = int(input())
# a = []
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     rank = 1
#     for j in range(n):
#         if bigger(a[i], a[j]):
#             rank+=1
#     print(rank, end =" ")