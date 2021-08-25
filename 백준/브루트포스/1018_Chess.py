# 슬라이싱을 이용하여 문자열을 8 x 8 2차원 배열로 잘라낸다
# chess 함수를 이용하여 최소 수정 개수를 구한다
# chess 함수는  [0][0]의 값을 기준으로 하여 최솟값을 구한다.


def chess(a):
    countB = 0
    countW = 0
    for i in range(4):
        for j in range(4):
            if a[2*i][2*j] != "B":
                countB +=1
            if a[2*i+1][2*j+1] != "B":
                countB += 1
            if a[2*i][2*j+1] == "B":
                countB += 1
            if a[2*i+1][2*j] == "B":
                countB +=1

    for i in range(4):
        for j in range(4):
            if a[2*i][2*j] != "W":
                countW +=1
            if a[2*i+1][2*j+1] != "W":
                countW += 1
            if a[2*i][2*j+1] == "W":
                countW += 1
            if a[2*i+1][2*j] == "W":
                countW +=1
    return min(countB, countW)




m, n = map(int, input().split())
a=[]

for i in range(m):
    a.append(input())
b = []
mn = m*n
for i in range(m - 7):
    for k in range(n - 7):
        for j in range(8):
            b.append(a[i:i+8][j][k:k+8])
        mn = min(mn, chess(b))
        b =[]
print(mn)



# 수정 사항
# 해결 알고리즘은 같지만 코드를 간단하게 써보자
# 슬라이싱을 하지 않고도 가능하다
# 슬라이싱하면 for문이 5중첩,,

# m, n = map(int, input().split())
# a = []
# count = []
# for i in range(m):
#     a.append(input())
# 
#
# for i in range(m - 7):
#     for j in range(n - 7):
#         countB = 0
#         countW = 0
#         for k in range(i,i+8):
#             for l in range(j,j+8):
#                 #count 함수를 간단하게 쓴거
#                 if(k+l)%2 == 0:
#                     if a[k][l] != "B":
#                         countB += 1
#                     if a[k][l] != "W":
#                         countW += 1
#                 if(k+l)%2 == 1:
#                     if a[k][l] == "B":
#                         countB += 1
#                     if a[k][l] == "W":
#                         countW += 1
#         count.append(min(countB,countW))
#
#
# print(min(count))