from collections import Counter
def solution(X, Y):
    counter = Counter(X) & Counter(Y)
    if not counter: 
        return "-1"
    
    answer = ""
    for i in range(9, -1, -1):
        n = str(i)
        if n in counter:
            answer += n * counter[n]
    if (answer[0] == "0"):
        return "0"
    return answer
    
