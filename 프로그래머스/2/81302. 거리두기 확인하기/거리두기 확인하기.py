def solution(places):
    
    return [is_valid(place) for place in places]


def is_valid(place):
    dy1 = [0, 0, 1, -1]
    dx1 = [1, -1, 0, 0]
    
    dy2 = [0, 0, 2, -2]
    dx2 = [2, -2, 0, 0]
    
    dy3 = [1, 1, -1, -1]
    dx3 = [1, -1, 1, -1]
    
    
    for y in range(len(place)):
        for x in range(len(place[0])):
            if place[y][x] == "P":
                for k in range(4):
                    ny1 = y + dy1[k]
                    nx1 = x + dx1[k]
                    
                    if 0 <= ny1 < 5 and 0 <= nx1 < 5 and place[ny1][nx1] == "P":
                        return 0
                    
                    ny2 = y + dy2[k]
                    nx2 = x + dx2[k]
                    
                    if 0 <= ny2 < 5 and 0 <= nx2 < 5 and place[ny1][nx1] != "X" and place[ny2][nx2] == "P":
                        return 0
                    
                    ny3 = y + dy3[k]
                    nx3 = x + dx3[k]
                    if 0 <= ny3 < 5 and 0 <= nx3 < 5 and (place[ny3][x] != "X" or place[y][nx3] != "X") and place[ny3][nx3] == "P":
                        return 0
                    
                    
    return 1
                    
                    
                