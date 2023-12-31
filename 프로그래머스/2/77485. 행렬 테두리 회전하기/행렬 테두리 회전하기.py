def solution(rows, columns, queries):
    rc = [[row * columns + column + 1  for column in range(columns)] for row in range(rows)]
    answer = []
    
    for y1, x1, y2, x2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        change = []
        temp = rc[y1][x1]
        change.append(temp)
        for x in range(x1, x2):
            rc[y1][x + 1], temp = temp, rc[y1][x + 1]
            change.append(temp)
        
        for y in range(y1, y2):
            rc[y + 1][x2], temp = temp, rc[y + 1][x2]
            change.append(temp)
        
        for x in range(x2, x1, -1):
            rc[y2][x - 1], temp = temp, rc[y2][x - 1]
            change.append(temp)
        
        for y in range(y2, y1, -1):
            rc[y - 1][x1], temp = temp, rc[y - 1][x1]
            change.append(temp)

        answer.append(min(change))
        
                
    
    return answer