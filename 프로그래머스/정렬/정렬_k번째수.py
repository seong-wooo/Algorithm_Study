#상당히 쉬운문제였다.
#슬라이싱을 이용하여 문제를 해결한다.
#그런데 다른사람의 풀이는 1줄이다.
# 반성하자
def solution(array, commands):
    answer = []

    for ijk in commands:
        slice_list = array[ijk[0]-1:ijk[1]]
        slice_list.sort()
        answer.append(slice_list[ijk[2]-1])

    return answer

###다른사람의 풀이
#map과 lamda를 이용하여 구현하였다.

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


