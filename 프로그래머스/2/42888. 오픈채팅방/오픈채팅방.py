def solution(record):
    d = dict()
    mention = ["님이 나갔습니다.", "님이 들어왔습니다."]
    answer = []
    for r in record:
        s = r.split()
        
        if s[0] == "Leave":
            answer.append([s[1], 0])
        
        else:
            d[s[1]] = s[2]
            if s[0] == "Enter":
                answer.append([s[1], 1])
    

    return [d[k] + mention[v] for k, v in answer]
        
        
        