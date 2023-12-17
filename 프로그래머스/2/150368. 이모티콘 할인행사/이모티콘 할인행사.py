# dfs
# 각 emoticon이 40 30 20 10 일 때를 계산해야한다.
# 100 * 2 ** 14 -> 1600000

def solution(users, emoticons):
    users = list(map(lambda x: x + [0], users))
    
    return dfs(users, emoticons)
        
    
def dfs(users, emoticons):
    if not emoticons:
        plus = 0
        total_sale = 0
        
        for user in users:
            if user[2] >= user[1]:
                plus += 1
            else:
                total_sale += user[2]
        return [plus, total_sale]
        
    
    rate = [10,20,30,40]
    emoticon = emoticons[0]
    
    result = []
    for i in range(4):
        d_emoticon = emoticon * (1 - rate[i] / 100)
        add = []
        for j in range(len(users)):
            if users[j][0] <= rate[i]:
                users[j][2] += d_emoticon
                add.append(j)
        result.append(dfs(users, emoticons[1:]))
        
        for a in add:
            users[a][2] -= d_emoticon
    
    
    result.sort(key = lambda x : (-x[0], -x[1]))
    
    return result[0]

