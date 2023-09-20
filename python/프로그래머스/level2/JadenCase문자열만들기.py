# 공백이 여러 개 있을 경우를 생각하지 못하였다.
# 공백을 표시하기 위해 index 변수르 삽입했다.
def solution(s):
    index = 0
    a = []
    for i in range(len(s)):
        if s[i] != " ":
            index += 1
        else:
            index = 0
        a.append(index)

    result = ""
    for i in range(len(a)):
        if a[i] == 1:
            result += s[i].upper()
        else:
            result += s[i].lower()

    return result