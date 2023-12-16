def solution(book_time):
    book_time = sorted(list(map(changeTime, book_time)), key = lambda x: x[0])
    room = []
    
    for time in book_time:
        available = []
        
        for i in range(len(room)):
            if time[0] >= room[i]:
                available.append((i, room[i]))
        
        if available:
            index, value = min(available, key=lambda x:x [1])
            room[index] = time[1]
            
        else:
            room.append(time[1])
        
    return len(room)
                
    
    

def changeTime(book_time):
    start, end = book_time
    s_h, s_m = map(int, start.split(":"))
    e_h, e_m = map(int, end.split(":"))
    
    return [s_h * 60 + s_m, e_h * 60 + e_m + 10]
    