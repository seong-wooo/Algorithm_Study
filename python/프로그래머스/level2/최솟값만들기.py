# 내가 푼 풀이
def solution(A,B):
    A.sort()
    B.sort()
    result = 0
    for i in range(len(A)):
        result += A[i] * B[-1 - i]

    return result

# 더 간단하게 zip을 사용하여 나타낸 풀이
def solution(A,B):
    return sum(a*b for a,b in zip(sorted(A), sorted(B, reverse=True)))