from collections import deque

def solution(prices):
    q = deque()
    
    answer = [0] * len(prices)
    
    # 값, index
    for i in range(len(prices)):
        while q and q[-1][0] > prices[i]:
            price, index = q.pop()
            answer[index] = i - index
        q.append([prices[i], i])

    
    while q:
        index = q.popleft()[1]
        answer[index] = len(prices) - 1 - index
        
    return answer