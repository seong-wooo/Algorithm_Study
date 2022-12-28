# LCS에 관한 프로젝트를 하고나니 1분만에 풀었다.
# LCS 관련 프로젝트를 확인하자

str1 =" " + input()
str2 =" " + input()

a, b =  len(str1), len(str2)

graph = [[0]*a for _ in range(b)]

for i in range(1, b):
    for j in range(1, a):
        if str1[j] == str2[i]:
            graph[i][j] = 1 + graph[i-1][j-1]
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])

print(graph[b-1][a-1])