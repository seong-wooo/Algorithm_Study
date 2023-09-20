# 처음에 1의 개수를 세고 1씩 올려가며 같은 1의 개수를 가지는 수를 찾는다 
def solution(n):
    c = bin(n).count("1")
    result = n + 1
    while bin(result).count("1") != c:
        result += 1
    return result