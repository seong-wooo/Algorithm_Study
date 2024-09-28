def solution(book_time):
    book_time = sorted(list(map(change_min, book_time)), key=lambda x: (x[0], x[1]))
    
    print(book_time)
    answer = [book_time[0][1]]
    
    for i in range(1, len(book_time)):
        index = find_room(answer, book_time[i][0])
        if index == -1:
            answer.append(book_time[i][1])
        else:
            answer[index] = book_time[i][1]
    
    return len(answer)
                


def change_min(time):
    h1, m1 = map(int, time[0].split(":"))
    h2, m2 = map(int, time[1].split(":"))
    
    
    return [h1*60+m1, h2*60+m2]


def find_room(answer, time):
    for i in range(len(answer)):
        if answer[i] + 10 <= time:
            return i
    return -1
                