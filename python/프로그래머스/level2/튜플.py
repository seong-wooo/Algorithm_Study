# 나의 풀이
# 파싱이 너무 더러움
def solution(s):
    s = s.split("},")
    for i in range(len(s)):
        s[i] = s[i].replace("{","")
        s[i] = s[i].replace("}","")
    for j in range(len(s)):
        s[j] = list(map(int, s[j].split(",")))

    s.sort(key=lambda x:len(x))

    a = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in a:
                a.append(s[i][j])
                break
    return a


# 더 깔끔하게 파싱하기
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
