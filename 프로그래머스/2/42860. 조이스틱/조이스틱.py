def solution(name):
    i = 0
    total = sum(count(s) for s in name)
    answer = len(name) - 1
    
    while i < len(name):
        j = i + 1
        while j < len(name) and name[j] == "A":
            j += 1

        if j == len(name):
            answer = min(answer, i)
        
        else:
            answer = min(answer, i * 2 + len(name) - j, (len(name) - j) * 2 + i)
        
        i = j

    return answer + total


#BBBBAAAABA
# i, j 가 정해진 경우 -> 1. 그냥 직진 하는 경우 2. i만큼 갔다가 뒤로 빠꾸, j만큼 뒤로 갔다가 다시 i만큼 전진

            

def count(a):
    n = ord(a)
    return min(n - 65, 91 - n)