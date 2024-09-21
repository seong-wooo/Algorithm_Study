# 약수를 구한다
# 약수 중 자기 제외 가장 큰 수를 넣는다

def solution(begin, end):
    answer = [0] * (end - begin + 1)
    
    
    for n in range(begin, end + 1):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                r = n // i
                if r <= 10_000_000:
                    answer[n-begin] = r
                    break
                else:
                    answer[n-begin] = i
                
                
        if answer[n-begin] == 0 and n > 1:
            answer[n-begin] = 1
    
    return answer
    