def solution(dirs):    
    d = {
        "U" : (1, 0),
        "L" : (0, -1),
        "R" : (0, 1),
        "D" : (-1, 0)
    }
    
    y, x = 5, 5
    visited = set()
    
    for dir in dirs:
        dy, dx = d[dir]
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < 11 and 0 <= nx < 11:
            visited.add((y, x, ny, nx))
            visited.add((ny, nx, y, x))
            y, x = ny, nx
    
    return len(visited) // 2