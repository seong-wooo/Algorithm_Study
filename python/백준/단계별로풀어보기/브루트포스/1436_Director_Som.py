# 문자열의 특성을 이용하여 순차적으로 666이 존재하는지 검사한다
# 간단하게 해결 가능했던 문제

n = int(input())

i = 665
while n > 0:
    i += 1
    if "666" in str(i):
        n -= 1
print(i)

