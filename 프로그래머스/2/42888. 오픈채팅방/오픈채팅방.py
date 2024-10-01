def solution(record):

    answer = []
    name = {}
    
    for r in record:
        command, *uid = r.split()

        if command == "Change":
            name[uid[0]] = uid[1]
        
        if command == "Enter":
            name[uid[0]] = uid[1]
            answer.append((uid[0], "님이 들어왔습니다."))
            
        elif command == "Leave":
            answer.append((uid[0], "님이 나갔습니다."))
    

    return list(map(lambda x: name[x[0]] + x[1], answer))
        
         