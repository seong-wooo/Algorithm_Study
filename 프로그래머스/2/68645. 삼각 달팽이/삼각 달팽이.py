def solution(n):
    result = [[0] * i for i in range(1, n+1)]
    direction = [(1, 0), (0, 1), (-1,-1)]
    d = 0
    count = n
    i = 1
    y, x = -1, 0
    
    while count > 0:
        for round_count in range(count):
            y,x = y + direction[d][0], x + direction[d][1]
            result[y][x] = i
            i += 1
        count -= 1
        d = (d+1)%3    
        
    answer =[]
    for r in result:
        answer += r
    return answer