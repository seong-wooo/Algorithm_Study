def solution(begin, end):
    answer = [0] + [1]* (end - begin) if begin == 1 else [1] * (end - begin + 1)
    
    
    for i in range(begin, end + 1):
        for n in range(2, min(10000000, int(i ** 0.5) + 1)):
            if i % n == 0:
                answer[i - begin] = max(answer[i-begin], i // n) if i // n <= 10000000 else max(answer[i-begin], n)
    
    return answer
