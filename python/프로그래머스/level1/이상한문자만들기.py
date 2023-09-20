def solution(s):
    i = 0
    result = ""
    for alpha in s:
        if alpha == " ":
            result += " "
            i = 0
        elif i % 2== 0:
            result += alpha.upper()
            i += 1
        else:
            result += alpha.lower()
            i+=1
    return result