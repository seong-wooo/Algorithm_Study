# 8개 확인
# x = 0, x = m, y = 0, y = n
# (y,x) = (0,0), (n, 0), (n, m), (0, m)




def solution(m, n, startX, startY, balls):
        
    starts = [
            [-startX, startY], # 왼쪽 |
            [startX, 2 * n - startY], # 위 ㅡ
            [2 * m - startX, startY], # 오른쪽 |
            [startX, -startY], # 아래 ㅡ
        ]     
    answer =[]
    for ball in balls:
        minimum = 1e9
        calc = [0,1,2,3]
            
        if startX == ball[0]:
            if startY > ball[1]:
                calc = [0,1,2]
            else:
                calc = [0,2,3]
        
        if startY == ball[1]:
            if startX > ball[0]:
                calc = [1,2,3]
            else:
                calc = [0,1,3]
        
        for c in calc:
            start_x, start_y = starts[c]
            minimum = min(minimum, (start_x - ball[0]) ** 2 + (start_y - ball[1]) ** 2)
        
        answer.append(minimum)
    
    return answer
        
