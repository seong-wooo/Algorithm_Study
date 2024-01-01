def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    
    node = 1
    y, x = 0, 0
    count = 0
    
    while count < n:
        for i in range(n - count):
            answer[y][x] = node
            node += 1
            if i != n - count - 1:
                y += dy[count % 3]
                x += dx[count % 3]
        count += 1
        y += dy[count % 3]
        x += dx[count % 3]

    
    return sum(answer, [])
    