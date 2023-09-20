#나의 코드
#문제점: 이진법을 직접 구현하였음..
#브루트 포스 방식의 시간 복잡도,,,
def bin(num):
    result = ""
    while num:
        num, m = num // 2, num % 2
        result = str(m) + result
    return result


def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        a, b = bin(arr1[i]).zfill(n), bin(arr2[i]).zfill(n)
        shap = ""
        for j in range(n):
            if a[j] == "1" or b[j] == "1":
                shap += "#"
            else:
                shap += " "
        result.append(shap)

    return result

#깔끔한 다른사람의 풀이
# rjust 원래 문자열을 오른쪽으로 미루고
# 앞에 2번째 parameter를 채움
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = bin(i|j)[2:]
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

