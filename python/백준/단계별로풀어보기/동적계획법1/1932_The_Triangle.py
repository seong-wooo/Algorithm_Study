# 1149번 문제와 거의 흡사한 문제이다.
# 매 단계마다 정보를 저장한다
# 저장된 정보를 이용하여 다음 단계에서 활용한다.
# dynamic programing

n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))