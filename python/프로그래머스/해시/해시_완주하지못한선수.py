# 나의 풀이
# Counter 함수를 이용하여 개수가 다른 것을 골라냈다.

from collections import Counter
def solution(participant, completion):
    answer = ''
    c_p = Counter(participant)
    c_c = Counter(completion)
    for i in c_p:
        if c_p[i] != c_c[i]:
            answer = i
            break
    return answer

# 다른사람의 풀이
# 마찬가지로 Counter 함수로 구현했지만 - 연산을 이용하여 더 짧게 썻다.
#
# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# 그런데 따지고 보면 for 문 중간에 break 를 하여 전체 연산을 안해도 되는 내 코드가 더 좋을거같다.
